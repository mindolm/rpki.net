"""
(Re)Initialize SQL tables used by these programs.

$Id$

Copyright (C) 2009  Internet Systems Consortium ("ISC")

Permission to use, copy, modify, and distribute this software for any
purpose with or without fee is hereby granted, provided that the above
copyright notice and this permission notice appear in all copies.

THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH
REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
AND FITNESS.  IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT,
INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
PERFORMANCE OF THIS SOFTWARE.
"""

import subprocess, ConfigParser

for name in ("rpkid", "irdbd", "pubd"):

  try:
    cfg = ConfigParser.RawConfigParser()
    cfg.read("%s.conf" % name)
    username = cfg.get(name, "sql-username")
    database = cfg.get(name, "sql-database")
    password = cfg.get(name, "sql-password")

  except:
    print "Cleaner couldn't read %s config file, ignoring" % name
    continue

  subprocess.check_call(("mysql", "-u", username, "-p" + password, database), stdin = open("../rpkid/%s.sql" % name))
