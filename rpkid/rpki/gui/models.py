"""
$Id$

Copyright (C) 2012  SPARTA, Inc. a Parsons Company

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND SPARTA DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS.  IN NO EVENT SHALL SPARTA BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.

Common classes for reuse in apps.
"""

import struct

from django.db import models

import rpki.resource_set
import rpki.ipaddrs

class IPv6AddressField(models.Field):
    "Field large enough to hold a 128-bit unsigned integer."

    __metaclass__ = models.SubfieldBase

    def db_type(self, connection):
        return 'binary(16)'

    def to_python(self, value):
        if isinstance(value, rpki.ipaddrs.v6addr):
            return value
        x = struct.unpack('!QQ', value)
        return rpki.ipaddrs.v6addr((x[0] << 64) | x[1])

    def get_db_prep_value(self, value, connection, prepared):
        return struct.pack('!QQ', (long(value) >> 64) & 0xFFFFFFFFFFFFFFFFL, long(value) & 0xFFFFFFFFFFFFFFFFL)

class IPv4AddressField(models.Field):
    "Wrapper around rpki.ipaddrs.v4addr."

    __metaclass__ = models.SubfieldBase

    def db_type(self, connection):
        return 'int UNSIGNED'

    def to_python(self, value):
        if isinstance(value, rpki.ipaddrs.v4addr):
            return value
        return rpki.ipaddrs.v4addr(value)

    def get_db_prep_value(self, value, connection, prepared):
        return long(value)

class Prefix(models.Model):
    """Common implementation for models with an IP address range.

    Expects that `range_cls` is set to the appropriate subclass of
    rpki.resource_set.resource_range_ip."""

    def as_resource_range(self):
        """
        Returns the prefix as a rpki.resource_set.resource_range_ip object.
        """
        return self.range_cls(self.prefix_min, self.prefix_max)

    def prefixlen(self):
        "Returns the prefix length for the prefix in this object."
        return self.as_resource_range().prefixlen()

    def get_prefix_display(self):
        "Return a string representatation of this IP prefix."
        return str(self.as_resource_range())

    def __unicode__(self):
        """This method may be overridden by subclasses.  The default
        implementation calls get_prefix_display(). """
        return self.get_prefix_display()

    class Meta:
        abstract = True
        
        # default sort order reflects what "sh ip bgp" outputs
        ordering = ('prefix_min',)

class PrefixV4(Prefix):
    "IPv4 Prefix."

    range_cls = rpki.resource_set.resource_range_ipv4

    prefix_min = IPv4AddressField(db_index=True, null=False)
    prefix_max = IPv4AddressField(db_index=True, null=False)

    class Meta(Prefix.Meta):
        abstract = True

class PrefixV6(Prefix):
    "IPv6 Prefix."

    range_cls = rpki.resource_set.resource_range_ipv6

    prefix_min = IPv6AddressField(db_index=True, null=False)
    prefix_max = IPv6AddressField(db_index=True, null=False)

    class Meta(Prefix.Meta):
        abstract = True

# vim:sw=4 ts=8 expandtab
