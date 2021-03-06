# $Id$
#
# Copyright (C) 2015-2016  Parsons Government Services ("PARSONS")
# Portions copyright (C) 2013-2014  Dragon Research Labs ("DRL")
# Portions copyright (C) 2011-2012  Internet Systems Consortium ("ISC")
#
# Permission to use, copy, modify, and distribute this software for any
# purpose with or without fee is hereby granted, provided that the above
# copyright notices and this permission notice appear in all copies.
#
# THE SOFTWARE IS PROVIDED "AS IS" AND PARSONS, DRL, AND ISC DISCLAIM
# ALL WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS.  IN NO EVENT SHALL
# PARSONS, DRL, OR ISC BE LIABLE FOR ANY SPECIAL, DIRECT, INDIRECT, OR
# CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM LOSS
# OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT,
# NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION
# WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.

"""
Common Django ORM field classes.

Many of these are complex ASN.1 DER objects stored as binaray data,
since the only sane text representation would just be the Base64
encoding of the DER and thus would add no value.
"""

import logging

from django.db import models

import rpki.x509
import rpki.sundial

logger = logging.getLogger(__name__)


class EnumField(models.PositiveSmallIntegerField):
    """
    An enumeration type that uses strings in Python and small integers
    in SQL.
    """

    description = "An enumeration type"

    def __init__(self, *args, **kwargs):
        if isinstance(kwargs.get("choices"), (tuple, list)) and isinstance(kwargs["choices"][0], (str, unicode)):
            kwargs["choices"] = tuple(enumerate(kwargs["choices"], 1))
        # Might need something here to handle string-valued default parameter
        models.PositiveSmallIntegerField.__init__(self, *args, **kwargs)
        self.enum_i2s = dict(self.flatchoices)
        self.enum_s2i = dict((v, k) for k, v in self.flatchoices)

    def from_db_value(self, value, expression, connection, context):
        return self.enum_i2s.get(value, value)

    def to_python(self, value):
        value = super(EnumField, self).to_python(value)
        return self.enum_i2s.get(value, value)

    def get_prep_value(self, value):
        return self.enum_s2i.get(value, value)


class SundialField(models.DateTimeField):
    """
    A field type for our customized datetime objects.
    """

    description = "A datetime type using our customized datetime objects"

    def from_db_value(self, value, expression, connection, context):
        return self.to_python(value)

    def to_python(self, value):
        if isinstance(value, rpki.sundial.pydatetime.datetime):
            return rpki.sundial.datetime.from_datetime(
                models.DateTimeField.to_python(self, value))
        else:
            return value

    def get_prep_value(self, value):
        if isinstance(value, rpki.sundial.datetime):
            return value.to_datetime()
        else:
            return value


class BlobField(models.Field):
    """
    Old BLOB field type, predating Django's BinaryField type.

    Do not use, this is only here for backwards compatabilty during migrations.
    """

    description   = "Raw BLOB type without ASN.1 encoding/decoding"

    def __init__(self, *args, **kwargs):
        self.blob_type = kwargs.pop("blob_type", None)
        kwargs["serialize"] = False
        kwargs["blank"] = True
        kwargs["default"] = None
        models.Field.__init__(self, *args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(BlobField, self).deconstruct()
        del kwargs["serialize"]
        del kwargs["blank"]
        del kwargs["default"]
        return name, path, args, kwargs

    def db_type(self, connection):
        if self.blob_type is not None:
            return self.blob_type
        elif connection.settings_dict['ENGINE'] == "django.db.backends.mysql":
            return "LONGBLOB"
        elif connection.settings_dict['ENGINE'] == "django.db.backends.posgresql":
            return "bytea"
        else:
            return "BLOB"


# For reasons which now escape me, I had a few fields in the old
# hand-coded SQL which used MySQL type BINARY(20) to hold SKIs.
# Presumably this was so that I could then use those SKIs in indexes
# and searches, but apparently I never got around to that part.
#
# SKIs probably would be better stored as hex strings anyway, so not
# bothering with a separate binary type model for this.  Deal with
# this if and when it ever becomes an issue.


# DERField used to be a subclass of BlobField.  Try changing it to be
# a subclass of BinaryField instead, leave BlobField (for now) for
# backwards compatability during migrations,

class DERField(models.BinaryField):
    """
    Field class for DER objects, with automatic translation between
    ASN.1 and Python types.  This is an abstract class, concrete field
    classes are derived from it.
    """

    rpki_type = rpki.x509.DER_object

    def __init__(self, *args, **kwargs):
        kwargs["blank"] = True
        kwargs["default"] = None
        super(DERField, self).__init__(*args, **kwargs)

    def deconstruct(self):
        name, path, args, kwargs = super(DERField, self).deconstruct()
        del kwargs["blank"]
        del kwargs["default"]
        return name, path, args, kwargs

    def from_db_value(self, value, expression, connection, context):
        if value is not None:
            value = self.rpki_type(DER = str(value))
        return value

    def to_python(self, value):
        value = super(DERField, self).to_python(value)
        if value is not None and not isinstance(value, self.rpki_type):
            value = self.rpki_type(DER = str(value))
        return value

    def get_prep_value(self, value):
        if value is not None:
            value = value.get_DER()
        return super(DERField, self).get_prep_value(value)


class CertificateField(DERField):
    description = "X.509 certificate"
    rpki_type   = rpki.x509.X509

class RSAPrivateKeyField(DERField):
    description = "RSA keypair"
    rpki_type   = rpki.x509.RSA

KeyField = RSAPrivateKeyField

class PublicKeyField(DERField):
    description = "RSA keypair"
    rpki_type   = rpki.x509.PublicKey

class CRLField(DERField):
    description = "Certificate Revocation List"
    rpki_type   = rpki.x509.CRL

class PKCS10Field(DERField):
    description = "PKCS #10 certificate request"
    rpki_type   = rpki.x509.PKCS10

class ManifestField(DERField):
    description = "RPKI Manifest"
    rpki_type   = rpki.x509.SignedManifest

class ROAField(DERField):
    description = "ROA"
    rpki_type   = rpki.x509.ROA

class GhostbusterField(DERField):
    description = "Ghostbuster Record"
    rpki_type   = rpki.x509.Ghostbuster
