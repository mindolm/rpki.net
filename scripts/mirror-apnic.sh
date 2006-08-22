#!/bin/sh -

cd `dirname $0`

# old repository, no longer maintained
# wget --mirror --relative --no-parent ftp://ftp.apnic.net/pub/test-certs/

# new repository, theoretically maintained
rsync -avz rsync://repository.apnic.net/ repository.apnic.net/
