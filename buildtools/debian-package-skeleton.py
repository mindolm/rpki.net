# Generated by wrap-tree.py.  Needs hacking for things like
# maintaining the debian/changelog file, but at least this gets all
# the debian/ubuntu stuff to date into the repository.

import os

os.makedirs('debian')

with open('debian/changelog', "wb") as f:
  f.write('''\
rpki (0.5126) UNRELEASED; urgency=low
  * Michael's replacement rpki-ca.postinst, with minor changes.
 -- sra <sra@rpki.net>  Sat, 09 Mar 2013 03:36:28 -0000

rpki (0.5125) UNRELEASED; urgency=low
  * rsync is a build dependency because ./configure says it is.
 -- sra <sra@rpki.net>  Fri, 08 Mar 2013 21:29:17 -0000

rpki (0.5124) UNRELEASED; urgency=low
  * Whack OpenSSL configuration to pull its notion of the CPU from
    autoconf rather than deducing this on its own, so that we can use
    pbuilder and pbuilder-dist to build both 32-bit and 64-bit
    packages on the same 64-bit Ubuntu machine.  See #423.
 -- sra <sra@rpki.net>  Fri, 08 Mar 2013 04:32:55 -0000

rpki (0.5123) UNRELEASED; urgency=low
  * Add mod_wsgi, enable mod_ssl.
 -- sra <sra@rpki.net>  Thu, 07 Mar 2013 20:03:55 -0000

rpki (0.5122) UNRELEASED; urgency=low
  * fix issue with automatically built config files
 -- melkins <melkins@rpki.net>  Thu, 07 Mar 2013 19:44:56 -0000

rpki (0.5121) UNRELEASED; urgency=low
  * pbuilder doesn't provide enough clues for us to guess that we need
    to use --install-layout=deb, so add ./configure option to force
    it.
 -- sra <sra@rpki.net>  Thu, 07 Mar 2013 19:31:47 -0000

rpki (0.5120) UNRELEASED; urgency=low
  * use --enable-target-install framework to add install-linux to the
    install target for the web portal
 -- melkins <melkins@rpki.net>  Thu, 07 Mar 2013 18:47:07 -0000

rpki (0.5119) UNRELEASED; urgency=low
  * move installation of most portal-gui scripts to setup.py (see
    #373)

    add script to be invoked by cron to download routeviews data

    add install-linux target for creating cron jobs for some rpki gui
    tasks
 -- melkins <melkins@rpki.net>  Thu, 07 Mar 2013 18:33:41 -0000

rpki (0.5118) UNRELEASED; urgency=low
  * Add "Section: net" header to debian/control; fixes #449.  Make
    both RPKI packages depend on apache2; fixes #445.  Get rid of "pip
    install" hack and change back to proper depends on Django and
    South to work properly with project APT repository; see #423.
    mod_ssl ("a2enmod ssl") and mod_wsgi not handled yet, get those
    tomorrow.
 -- sra <sra@rpki.net>  Thu, 07 Mar 2013 07:20:35 -0000

rpki (0.5117) UNRELEASED; urgency=low
  * Relax South requirement to version 0.7.5, per Michael's testing.
    Closes #450.
 -- sra <sra@rpki.net>  Thu, 07 Mar 2013 07:04:27 -0000

rpki (0.5116) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Thu, 07 Mar 2013 02:00:11 -0000

rpki (0.5115) UNRELEASED; urgency=low
  * fix typoh
 -- melkins <melkins@rpki.net>  Wed, 06 Mar 2013 23:26:45 -0000

rpki (0.5114) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Wed, 06 Mar 2013 18:00:09 -0000

rpki (0.5113) UNRELEASED; urgency=low
  * display error message if username was omitted when specifying
    --enable-wsgi-daemon-mode
 -- melkins <melkins@rpki.net>  Wed, 06 Mar 2013 17:28:54 -0000

rpki (0.5112) UNRELEASED; urgency=low
  * fix DeprecationWarning showing up in the apache.log

    see #447
 -- melkins <melkins@rpki.net>  Wed, 06 Mar 2013 17:16:49 -0000

rpki (0.5111) UNRELEASED; urgency=low
  * comment out debug statement printing sys.path

    see #447
 -- melkins <melkins@rpki.net>  Wed, 06 Mar 2013 17:06:46 -0000

rpki (0.5110) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Wed, 06 Mar 2013 07:00:16 -0000

rpki (0.5109) UNRELEASED; urgency=low
  * revert [5090]

    see #423
 -- melkins <melkins@rpki.net>  Wed, 06 Mar 2013 03:12:55 -0000

rpki (0.5108) UNRELEASED; urgency=low
  * revert [5096]

    see #438
 -- melkins <melkins@rpki.net>  Wed, 06 Mar 2013 03:09:49 -0000

rpki (0.5107) UNRELEASED; urgency=low
  * Skip synchronization for parents with no repository set.  Fixes
    #438.
 -- sra <sra@rpki.net>  Tue, 05 Mar 2013 15:20:34 -0000

rpki (0.5106) UNRELEASED; urgency=low
  * fix paginator template tag to nicely display when there are a huge
    amount of pages.  display at most 5 page links and use ellipsis to
    indicate there are more pages.
 -- melkins <melkins@rpki.net>  Tue, 05 Mar 2013 01:04:29 -0000

rpki (0.5105) UNRELEASED; urgency=low
  * need enctype="multipart/form-data" when uploading files in a form

    closes #392
 -- melkins <melkins@rpki.net>  Tue, 05 Mar 2013 00:17:09 -0000

rpki (0.5104) UNRELEASED; urgency=low
  * field label was not being expanded in the app_form.html template
 -- melkins <melkins@rpki.net>  Tue, 05 Mar 2013 00:16:24 -0000

rpki (0.5103) UNRELEASED; urgency=low
  * remove outdated css class attributes for an old version of
    bootstap
 -- melkins <melkins@rpki.net>  Tue, 05 Mar 2013 00:15:50 -0000

rpki (0.5102) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Tue, 05 Mar 2013 00:00:26 -0000

rpki (0.5101) UNRELEASED; urgency=low
  * remove deprecated script that was used back when the web portal
    used the sqlite db backend
 -- melkins <melkins@rpki.net>  Mon, 04 Mar 2013 23:03:14 -0000

rpki (0.5100) UNRELEASED; urgency=low
  * move core function to rpki.gui.app.check_expired

    see #442
 -- melkins <melkins@rpki.net>  Mon, 04 Mar 2013 22:54:47 -0000

rpki (0.5099) UNRELEASED; urgency=low
  * add .cert_chain property to return the complete certificate chain
    for the specified object
 -- melkins <melkins@rpki.net>  Mon, 04 Mar 2013 22:14:53 -0000

rpki (0.5098) UNRELEASED; urgency=low
  * move core of rpkid/portal-gui/scripts/rpkigui-import-routes.py to
    rpkid/rpki/gui/routeview/util.py

    see #442
 -- melkins <melkins@rpki.net>  Mon, 04 Mar 2013 21:02:43 -0000

rpki (0.5097) UNRELEASED; urgency=low
  * move core implementation to rpki.gui.cacheview.util and only leave
    the script wrapper

    see #442
 -- melkins <melkins@rpki.net>  Mon, 04 Mar 2013 19:41:55 -0000

rpki (0.5096) UNRELEASED; urgency=low
  * move build-time generated configuration to local_settings.py and
    leave settings.py as a static file
 -- melkins <melkins@rpki.net>  Sun, 03 Mar 2013 19:02:15 -0000

rpki (0.5095) UNRELEASED; urgency=low
  * remove duplication line of code
 -- melkins <melkins@rpki.net>  Fri, 01 Mar 2013 22:16:44 -0000

rpki (0.5094) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Fri, 01 Mar 2013 22:00:09 -0000

rpki (0.5093) UNRELEASED; urgency=low
  * change rpki.gui.models.IPV6AddressField.get_db_prep_value() to
    return `long` rather than a string

    add a custom encoder to the mysql database connection which
    converts long values to hex strings when generating SQL statements

    closes #434
 -- melkins <melkins@rpki.net>  Fri, 01 Mar 2013 18:50:03 -0000

rpki (0.5092) UNRELEASED; urgency=low
  * remove rpki.gui.cacheview from urls.py since it is outdated and
    doesn't compile with django 1.5

    see #433
 -- melkins <melkins@rpki.net>  Thu, 28 Feb 2013 17:50:36 -0000

rpki (0.5091) UNRELEASED; urgency=low
  * update templates for new syntax of the {% url %} tag in django 1.5
 -- melkins <melkins@rpki.net>  Thu, 28 Feb 2013 17:49:43 -0000

rpki (0.5090) UNRELEASED; urgency=low
  * if the django-admin script is not found, configure should exit and
    inform the user so they can correct their $PATH

    see #431
 -- melkins <melkins@rpki.net>  Thu, 28 Feb 2013 17:15:00 -0000

rpki (0.5089) UNRELEASED; urgency=low
  * Fix rcynic installation rules broken in packaging branch merge.
    Fixes #428 and 429.
 -- sra <sra@rpki.net>  Thu, 28 Feb 2013 01:10:14 -0000

rpki (0.5088) UNRELEASED; urgency=low
  * svn:ignore.
 -- sra <sra@rpki.net>  Thu, 28 Feb 2013 01:07:23 -0000

rpki (0.5087) UNRELEASED; urgency=low
  * conf list for superusers should show everything
 -- melkins <melkins@rpki.net>  Thu, 28 Feb 2013 00:14:34 -0000

rpki (0.5086) UNRELEASED; urgency=low
  * add new script rpkigui-flatten-roas script to take care of
    flattening old roas which had multiple prefixes

    see #421
 -- melkins <melkins@rpki.net>  Thu, 28 Feb 2013 00:07:35 -0000

rpki (0.5085) UNRELEASED; urgency=low
  * drop "Request" from "ROA Requests" in dashboard

    closes #419
 -- melkins <melkins@rpki.net>  Wed, 27 Feb 2013 22:51:21 -0000

rpki (0.5084) UNRELEASED; urgency=low
  * add a clone button to each roa, which copies the prefix as the
    default value when generating a new roa

    see #325
 -- melkins <melkins@rpki.net>  Wed, 27 Feb 2013 22:47:00 -0000

rpki (0.5083) UNRELEASED; urgency=low
  * updated web portal html templates to use newer syntax for the {%
    url %} tag
 -- melkins <melkins@rpki.net>  Wed, 27 Feb 2013 22:19:19 -0000

rpki (0.5082) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Tue, 26 Feb 2013 19:00:12 -0000

rpki (0.5081) UNRELEASED; urgency=low
  * add support for multiple users managing the same resource holder
 -- melkins <melkins@rpki.net>  Tue, 26 Feb 2013 18:57:15 -0000

rpki (0.5080) UNRELEASED; urgency=low
  * Create publication directory.
 -- sra <sra@rpki.net>  Tue, 26 Feb 2013 08:59:39 -0000

rpki (0.5079) UNRELEASED; urgency=low
  * Clean generated rpki.conf.sample.
 -- sra <sra@rpki.net>  Tue, 26 Feb 2013 06:04:50 -0000

rpki (0.5078) UNRELEASED; urgency=low
  * Sigh, I guess it would be too simple if @sharedstatedir@ had
    anything to do with /usr/share.  Apparently I really meant
    @datarootdir@.
 -- sra <sra@rpki.net>  Tue, 26 Feb 2013 04:22:28 -0000

rpki (0.5077) UNRELEASED; urgency=low
  * svn:ignore.
 -- sra <sra@rpki.net>  Tue, 26 Feb 2013 04:09:24 -0000

rpki (0.5076) UNRELEASED; urgency=low
  * Make ${sharedstatedir}/rpki/publication the default location for
    the publication tree.  Customize rpki.conf.sample to account for
    sharedstatedir setting.
 -- sra <sra@rpki.net>  Tue, 26 Feb 2013 03:49:58 -0000

rpki (0.5075) UNRELEASED; urgency=low
  * Need rpki.conf to start CA daemons.
 -- sra <sra@rpki.net>  Tue, 26 Feb 2013 02:28:57 -0000

rpki (0.5074) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Tue, 26 Feb 2013 02:00:20 -0000

rpki (0.5073) UNRELEASED; urgency=low
  * Make Django requirement consistent in doc and scripts: we now want
    1.3.7 or later.
 -- sra <sra@rpki.net>  Tue, 26 Feb 2013 01:20:37 -0000

rpki (0.5072) UNRELEASED; urgency=low
  * move repository client list to its own page

    closes #424
 -- melkins <melkins@rpki.net>  Mon, 25 Feb 2013 17:27:24 -0000

rpki (0.5071) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Mon, 25 Feb 2013 09:00:51 -0000

rpki (0.5069) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Mon, 25 Feb 2013 08:00:41 -0000

rpki (0.5067) UNRELEASED; urgency=low
  * Automatic pull of documentation from Wiki.
 -- docbot <docbot@rpki.net>  Mon, 25 Feb 2013 07:00:29 -0000

rpki (0.5065) UNRELEASED; urgency=low
  * Merge platform-specific packaging changes back to trunk.  Closes
    #377, #374, #395, #398.  Also see #373, which ended up not being
    covered by this branch after all.
 -- sra <sra@rpki.net>  Mon, 25 Feb 2013 03:58:36 -0000

rpki (0.5059) UNRELEASED; urgency=low
  * Not using MANIFEST.in.
 -- sra <sra@rpki.net>  Sun, 24 Feb 2013 03:24:07 -0000

rpki (0.5060) UNRELEASED; urgency=low
  * First build, then install, doh.
 -- sra <sra@rpki.net>  Sun, 24 Feb 2013 03:33:30 -0000

rpki (0.5059) UNRELEASED; urgency=low
  * Not using MANIFEST.in.
 -- sra <sra@rpki.net>  Sun, 24 Feb 2013 03:24:07 -0000

rpki (0.5058) UNRELEASED; urgency=low
  * inetd/xinetd listener for rpki-rtr on source code installation,
    also needed for Ubuntu package.
 -- sra <sra@rpki.net>  Sun, 24 Feb 2013 03:22:00 -0000

rpki (0.5057) UNRELEASED; urgency=low
  * Add dependency on xinetd.
 -- sra <sra@rpki.net>  Sat, 23 Feb 2013 13:25:46 -0000

rpki (0.5056) UNRELEASED; urgency=low
  * More post-installation: add rpki-rtr listener to /etc/services and
    /etc/inetd.conf, create a few missing directories.
 -- sra <sra@rpki.net>  Sat, 23 Feb 2013 12:22:10 -0000

rpki (0.5054) UNRELEASED; urgency=low
  * Hack to use pip to install recent versions of Django and South.
    Probably should be replaced by our own APT repository at some
    point, but this seems to work.
 -- sra <sra@rpki.net>  Fri, 22 Feb 2013 03:48:54 -0000

rpki (0.5051) UNRELEASED; urgency=low
  * Pull from trunk.
 -- sra <sra@rpki.net>  Thu, 21 Feb 2013 01:17:22 -0000

rpki (0.5047) UNRELEASED; urgency=low
  * Pull from trunk.
 -- sra <sra@rpki.net>  Wed, 20 Feb 2013 08:31:58 -0000

rpki (0.5045) UNRELEASED; urgency=low
  * Pull from trunk.
 -- sra <sra@rpki.net>  Wed, 20 Feb 2013 01:31:40 -0000

rpki (0.5042) UNRELEASED; urgency=low
  * Get rid of silly "r" prefix on version number for FreeBSD
    packages, among other reasons so that we can have the same version
    numbers on FreeBSD and Ubuntu, doh.
 -- sra <sra@rpki.net>  Tue, 19 Feb 2013 02:20:28 -0000

rpki (0.5041) UNRELEASED; urgency=low
  * Install generated debian/changelog, now that we generate ones that
    debuild accepts.
 -- sra <sra@rpki.net>  Mon, 18 Feb 2013 07:17:57 -0000

rpki (0.5040) UNRELEASED; urgency=low
  * debuild et al are picky about format of email addresses.

    For some reason debuild now cares about "make test" failing (which
    it always has on package builds, because of MySQL setup
    requirements, but debuild used to ignore that), so tweak rules to
    skip the test suite.
 -- sra <sra@rpki.net>  Mon, 18 Feb 2013 06:58:51 -0000

rpki (0.5039) UNRELEASED; urgency=low
  * Script to automate debian/changelogs.
 -- sra <sra@rpki.net>  Mon, 18 Feb 2013 05:46:00 -0000

rpki (0.5038) UNRELEASED; urgency=low
  * Add rc.d script.
 -- sra <sra@rpki.net>  Sun, 17 Feb 2013 10:05:49 -0000

rpki (0.5037) UNRELEASED; urgency=low
  * Debug pkg-plist generation.
 -- sra <sra@rpki.net>  Mon, 11 Feb 2013 05:27:59 -0000

rpki (0.5036) UNRELEASED; urgency=low
  * pkg-plist generation hacks.
 -- sra <sra@rpki.net>  Mon, 11 Feb 2013 03:04:05 -0000

rpki (0.5035) UNRELEASED; urgency=low
  * Pull from trunk.
 -- sra <sra@rpki.net>  Mon, 11 Feb 2013 02:25:18 -0000

rpki (0.5034) UNRELEASED; urgency=low
  * Add --disable-rp-tools, for package building.
 -- sra <sra@rpki.net>  Mon, 11 Feb 2013 02:18:42 -0000

rpki (0.5030) UNRELEASED; urgency=low
  * Pull from trunk.
 -- sra <sra@rpki.net>  Tue, 05 Feb 2013 21:04:06 -0000

rpki (0.5028) UNRELEASED; urgency=low
  * Run daemons as root for now, come back to permission issues when
    everything else works as expected.
 -- sra <sra@rpki.net>  Tue, 05 Feb 2013 04:41:02 -0000

rpki (0.5027) UNRELEASED; urgency=low
  * Clean up debian/ directory, enable upstart.
 -- sra <sra@rpki.net>  Tue, 05 Feb 2013 00:12:49 -0000

rpki (0.5026) UNRELEASED; urgency=low
  * Install sample rpki.conf, since we don't (yet?) have a good way to
    generate one automatically during installation.  Installation
    dialog is probably not the right way to go, some kind of setup
    wizard script for the user to run after installation is probably a
    better bet.
 -- sra <sra@rpki.net>  Mon, 04 Feb 2013 23:09:34 -0000

rpki (0.5025) UNRELEASED; urgency=low
  * Tweak directory ownerships on Debian install, and add a few more
    bits to rpki-ca.upstart while we're at it.
 -- sra <sra@rpki.net>  Mon, 04 Feb 2013 05:36:12 -0000

rpki (0.5024) UNRELEASED; urgency=low
  * Allow naming tree(s) on command line.
 -- sra <sra@rpki.net>  Mon, 04 Feb 2013 05:31:03 -0000

rpki (0.5023) UNRELEASED; urgency=low
  * Wrapped debian skeleton.
 -- sra <sra@rpki.net>  Sun, 03 Feb 2013 22:27:01 -0000

rpki (0.5022) UNRELEASED; urgency=low
  * Helper for generating package skeletons.
 -- sra <sra@rpki.net>  Sun, 03 Feb 2013 22:15:47 -0000

rpki (0.5021) UNRELEASED; urgency=low
  * Checkpoint.
 -- sra <sra@rpki.net>  Sun, 03 Feb 2013 17:02:21 -0000

rpki (0.5020) UNRELEASED; urgency=low
  * Change default location of rcynic-html output on FreeBSD to track
    the current FreeBSD Apache default, silly though that location may
    be. Thanks, Jay!
 -- sra <sra@rpki.net>  Sun, 03 Feb 2013 16:41:33 -0000

rpki (0.5019) UNRELEASED; urgency=low
  * Don't try to run rcynic-html if parent output directory doesn't
    exist.
 -- sra <sra@rpki.net>  Sun, 03 Feb 2013 16:36:45 -0000

rpki (0.5018) UNRELEASED; urgency=low
  * Doh, don't put  in generated rcynic.conf.
 -- sra <sra@rpki.net>  Sun, 03 Feb 2013 16:25:18 -0000

rpki (0.5017) UNRELEASED; urgency=low
  * Cleanup
 -- sra <sra@rpki.net>  Sun, 03 Feb 2013 05:38:42 -0000

rpki (0.5016) UNRELEASED; urgency=low
  * Seems /var/run is a temporary filesystem on some platforms.
 -- sra <sra@rpki.net>  Sun, 03 Feb 2013 02:07:39 -0000

rpki (0.5015) UNRELEASED; urgency=low
  * Typo in pkg-deinstall.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 19:46:33 -0000

rpki (0.5014) UNRELEASED; urgency=low
  * Exit without whining when another process holds the lock.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 19:08:34 -0000

rpki (0.5013) UNRELEASED; urgency=low
  * Wire installed location of scan_roas into installed rtr-origin, so
    that we can stop fighting with FreeBSD's odd habit of installing
    packaged software in /usr/local/bin while excluding /usr/local/bin
    from the default $PATH in system cron jobs and shell scripts.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 19:02:11 -0000

rpki (0.5012) UNRELEASED; urgency=low
  * Need rsync as both build and runtime dependency.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 08:34:30 -0000

rpki (0.5011) UNRELEASED; urgency=low
  * OK, now I know why nobody ever uses "install -C".
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 08:19:35 -0000

rpki (0.5010) UNRELEASED; urgency=low
  * rcynic requires rsync, doh.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 07:56:31 -0000

rpki (0.5009) UNRELEASED; urgency=low
  * Fun with DESTDIR.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 07:22:08 -0000

rpki (0.5008) UNRELEASED; urgency=low
  * Beat FreeBSD packaging stuff with a club.  Might be working now.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 06:58:53 -0000

rpki (0.5007) UNRELEASED; urgency=low
  * Whoops, ac_* variables are lowercase this week.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 06:58:27 -0000

rpki (0.5006) UNRELEASED; urgency=low
  * Doh, write TAL configuration to correct file.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 05:37:46 -0000

rpki (0.5005) UNRELEASED; urgency=low
  * etc/rc.d/rcynic is only for jails, so it's not in the port
    anymore.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 05:29:03 -0000

rpki (0.5004) UNRELEASED; urgency=low
  * Whack FreeBSD port skeleton to track recent changes.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 05:00:27 -0000

rpki (0.5003) UNRELEASED; urgency=low
  * First round of fixes to installation targets.
 -- sra <sra@rpki.net>  Sat, 02 Feb 2013 04:15:51 -0000

rpki (0.5002) UNRELEASED; urgency=low
  * Finally ready to start testing new rcynic install code.
 -- sra <sra@rpki.net>  Fri, 01 Feb 2013 21:50:18 -0000

rpki (0.5001) UNRELEASED; urgency=low
  * Checkpoint
 -- sra <sra@rpki.net>  Fri, 01 Feb 2013 18:38:48 -0000

rpki (0.5000) UNRELEASED; urgency=low
  * Cleanup.
 -- sra <sra@rpki.net>  Fri, 01 Feb 2013 13:22:19 -0000

rpki (0.4999) UNRELEASED; urgency=low
  * chown() lock file to rcynic user when creating it as root.
 -- sra <sra@rpki.net>  Fri, 01 Feb 2013 05:08:08 -0000

rpki (0.4998) UNRELEASED; urgency=low
  * Add rcynic-cron.
 -- sra <sra@rpki.net>  Fri, 01 Feb 2013 03:17:34 -0000

rpki (0.4997) UNRELEASED; urgency=low
  * Merge from trunk.
 -- sra <sra@rpki.net>  Thu, 31 Jan 2013 22:10:02 -0000

rpki (0.4995) UNRELEASED; urgency=low
  * Checkpoint
 -- sra <sra@rpki.net>  Thu, 31 Jan 2013 21:56:29 -0000

rpki (0.4989) UNRELEASED; urgency=low
  * Pull from trunk.
 -- sra <sra@rpki.net>  Thu, 31 Jan 2013 05:04:39 -0000

rpki (0.4988) UNRELEASED; urgency=low
  * Checkpoint
 -- sra <sra@rpki.net>  Thu, 31 Jan 2013 05:03:04 -0000

rpki (0.4980) UNRELEASED; urgency=low
  * Pull from trunk.
 -- sra <sra@rpki.net>  Fri, 25 Jan 2013 07:41:00 -0000

rpki (0.4978) UNRELEASED; urgency=low
  * Pull from trunk.
 -- sra <sra@rpki.net>  Fri, 25 Jan 2013 05:09:38 -0000

rpki (0.4976) UNRELEASED; urgency=low

  * Test update to changelog.

 -- Rob Austein <sra@hactrn.net>  Tue, 22 Jan 2013 02:50:01 -0500

rpki (0.4968) UNRELEASED; urgency=low

  * Initial Release.

 -- Rob Austein <sra@hactrn.net>  Tue, 15 Jan 2013 13:29:54 -0500
''')

with open('debian/compat', "wb") as f:
  f.write('''\
8
''')

with open('debian/control', "wb") as f:
  f.write('''\
# python-django should be at least 1.3.7, but we don't support 1.5 yet (see #443), so for now ask for something lower than 1.5 and hope for the best.

Source: rpki
Section: net
Priority: extra
Maintainer: Rob Austein <sra@hactrn.net>
Build-Depends: debhelper (>= 8.0.0), autotools-dev, rsync, xsltproc, python (>= 2.7), python-all-dev, python-setuptools, python-lxml, libxml2-utils, mysql-client, mysql-server, python-mysqldb, python-vobject, python-yaml, python-django (<< 1.5), python-django-south (>= 0.7.5)
Standards-Version: 3.9.3
Homepage: http://trac.rpki.net/
Vcs-Svn: http://subvert-rpki.hactrn.net/
Vcs-Browser: http://trac.rpki.net/browser

Package: rpki-rp
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, python (>= 2.7), rrdtool, rsync, xinetd, apache2
Description: rpki.net relying party tools
 "Relying party" validation tools from the rpki.net toolkit.
 See the online documentation at http://rpki.net/.

Package: rpki-ca
Architecture: any
Depends: ${shlibs:Depends}, ${misc:Depends}, xsltproc, python (>= 2.7), python-lxml, libxml2-utils, mysql-client, mysql-server, python-mysqldb, python-vobject, python-yaml, python-django (<< 1.5), python-django-south (>= 0.7.5), apache2, libapache2-mod-wsgi
Description: rpki.net certification authority tools
 "Certification authority" tools for issuing RPKI certificates and
 related objects using the rpki.net toolkit.
 See the online documentation at http://rpki.net/.
''')

with open('debian/copyright', "wb") as f:
  f.write('''\
Format: http://dep.debian.net/deps/dep5
Upstream-Name: rpki
Source: http://rpki.net/


Files: *
Copyright: 2006-2008 American Registry for Internet Numbers
	   2009-2013 Internet Systems Consortium
	   2010-2013 SPARTA, Inc.
License: ISC


Files: openssl/openssl-*.tar.gz
Copyright: 1998-2012 The OpenSSL Project
	   1995-1998 Eric A. Young, Tim J. Hudson
License: OpenSSL and SSLeay


License: ISC
 Permission to use, copy, modify, and distribute this software for any
 purpose with or without fee is hereby granted, provided that the above
 copyright notice and this permission notice appear in all copies.
 .
 THE SOFTWARE IS PROVIDED "AS IS" AND ISC DISCLAIMS ALL WARRANTIES WITH
 REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES OF MERCHANTABILITY
 AND FITNESS.  IN NO EVENT SHALL ISC BE LIABLE FOR ANY SPECIAL, DIRECT,
 INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY DAMAGES WHATSOEVER RESULTING FROM
 LOSS OF USE, DATA OR PROFITS, WHETHER IN AN ACTION OF CONTRACT, NEGLIGENCE
 OR OTHER TORTIOUS ACTION, ARISING OUT OF OR IN CONNECTION WITH THE USE OR
 PERFORMANCE OF THIS SOFTWARE.


License: OpenSSL
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 .
 1. Redistributions of source code must retain the above copyright
    notice, this list of conditions and the following disclaimer. 
 .
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in
    the documentation and/or other materials provided with the
    distribution.
 .
 3. All advertising materials mentioning features or use of this
    software must display the following acknowledgment:
    "This product includes software developed by the OpenSSL Project
    for use in the OpenSSL Toolkit. (http://www.OpenSSL.org/)"
 .
 4. The names "OpenSSL Toolkit" and "OpenSSL Project" must not be used to
    endorse or promote products derived from this software without
    prior written permission. For written permission, please contact
    licensing@OpenSSL.org.
 .
 5. Products derived from this software may not be called "OpenSSL"
    nor may "OpenSSL" appear in their names without prior written
    permission of the OpenSSL Project.
 .
 6. Redistributions of any form whatsoever must retain the following
    acknowledgment:
    "This product includes software developed by the OpenSSL Project
    for use in the OpenSSL Toolkit (http://www.OpenSSL.org/)"
 .
 THIS SOFTWARE IS PROVIDED BY THE OpenSSL PROJECT ``AS IS'' AND ANY
 EXPRESSED OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
 PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE OpenSSL PROJECT OR
 ITS CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
 SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT
 NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT,
 STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED
 OF THE POSSIBILITY OF SUCH DAMAGE.
 .
 This product includes cryptographic software written by Eric Young
 (eay@cryptsoft.com).  This product includes software written by Tim
 Hudson (tjh@cryptsoft.com).


License: SSLeay
 This library is free for commercial and non-commercial use as long as
 the following conditions are aheared to.  The following conditions
 apply to all code found in this distribution, be it the RC4, RSA,
 lhash, DES, etc., code; not just the SSL code.  The SSL documentation
 included with this distribution is covered by the same copyright terms
 except that the holder is Tim Hudson (tjh@cryptsoft.com).
 .
 Copyright remains Eric Young's, and as such any Copyright notices in
 the code are not to be removed.
 If this package is used in a product, Eric Young should be given attribution
 as the author of the parts of the library used.
 This can be in the form of a textual message at program startup or
 in documentation (online or textual) provided with the package.
 .
 Redistribution and use in source and binary forms, with or without
 modification, are permitted provided that the following conditions
 are met:
 1. Redistributions of source code must retain the copyright
    notice, this list of conditions and the following disclaimer.
 2. Redistributions in binary form must reproduce the above copyright
    notice, this list of conditions and the following disclaimer in the
    documentation and/or other materials provided with the distribution.
 3. All advertising materials mentioning features or use of this software
    must display the following acknowledgement:
    "This product includes cryptographic software written by
     Eric Young (eay@cryptsoft.com)"
    The word 'cryptographic' can be left out if the rouines from the library
    being used are not cryptographic related :-).
 4. If you include any Windows specific code (or a derivative thereof) from 
    the apps directory (application code) you must include an acknowledgement:
    "This product includes software written by Tim Hudson (tjh@cryptsoft.com)"
 .
 THIS SOFTWARE IS PROVIDED BY ERIC YOUNG ``AS IS'' AND
 ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 ARE DISCLAIMED.  IN NO EVENT SHALL THE AUTHOR OR CONTRIBUTORS BE LIABLE
 FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
 DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS
 OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
 HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY
 OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF
 SUCH DAMAGE.
 .
 The licence and distribution terms for any publically available version or
 derivative of this code cannot be changed.  i.e. this code cannot simply be
 copied and put under another distribution licence
 [including the GNU Public Licence.]
''')

with open('debian/rpki-ca.install', "wb") as f:
  f.write('''\
etc/rpki.conf.sample
etc/rpki/apache.conf
etc/rpki/settings.py
usr/lib
usr/sbin
usr/share
''')

with open('debian/rpki-ca.lintian-overrides', "wb") as f:
  f.write('''\
# The RPKI code requires a copy of the OpenSSL library with both the
# CMS code and RFC 3779 code enabled.  All recent versions of OpenSSL
# include this code, but it's not enabled on all platforms.  On Ubuntu
# 12.04 LTS, the RFC 3779 code is disabled.  So we take the least bad
# of our several bad options, and carefully link against a private
# copy of the OpenSSL crypto library built with the options we need,
# with all the voodoo necessary to avoid conflicts with, eg, the
# OpenSSL shared libraries that are already linked into Python.
#
# It would be totally awesome if the OpenSSL package maintainers were
# to enable the RFC 3779 code for us, but I'm not holding my breath.
#
# In the meantime, we need to tell lintian to allow this nasty hack.

rpki-ca: embedded-library
''')

with open('debian/rpki-ca.postinst', "wb") as f:
  f.write('''\
#!/bin/sh
# postinst script for rpki-ca
#
# see: dh_installdeb(1)

set -e

setup_rpkid_user() {
    if ! getent passwd rpkid >/dev/null
    then
	useradd -g rpkid -M -N -d /nonexistent -s /sbin/nologin -c "RPKI certification authority engine(s)" rpkid
    fi
}

setup_rpkid_group() {
    if ! getent group rpkid >/dev/null
    then
	groupadd rpkid
    fi
}

setup_apache() {
    # edit existing file
    f=/etc/apache2/sites-available/default-ssl
    conf=/etc/rpki/apache.conf
    cmd=no
    if test "x$(grep -q "[^#]*Include $conf" $f)" = "x"
    then
        awk < $f > ${f}.tmp -v conf=$conf '
	    $0 ~ /[^#]*<\\/VirtualHost>/ { print "Include", conf }
            { print }
	'
        if test ! -f ${f}.orig
        then
            ln $f ${f}.orig
        fi
        mv ${f}.tmp $f
        cmd=reload
    fi
    if test ! -f /etc/apache2/sites-enabled/default-ssl
    then
        a2ensite default-ssl
        cmd=reload
    fi
    if test ! -f /etc/apache2/mods-enabled/ssl.conf
    then
        a2enmod ssl
        cmd=restart
    fi
    if test $cmd != no
    then
        service apache2 $cmd
    fi
}

setup_django() {
    # we can't perform automatic upgrade when rpki.conf isn't present
    if test -f /etc/rpki.conf
    then
	rpki-manage syncdb
	rpki-manage migrate app
    fi
}

setup_cron() {
    t=$(hexdump -n 1 -e '"%u"' /dev/urandom) && echo "$(($t % 60)) 0/2 * * * nobody /usr/share/rpki/routeviews.sh" > /etc/cron.d/rpkigui-routeviews
    chmod 644 /etc/cron.d/rpkigui-routeviews
    ln -sf /usr/sbin/rpkigui-check-expired /etc/cron.daily/rpkigui-check-expired
}

# summary of how this script can be called:
#        * <postinst> `configure' <most-recently-configured-version>
#        * <old-postinst> `abort-upgrade' <new version>
#        * <conflictor's-postinst> `abort-remove' `in-favour' <package>
#          <new-version>
#        * <postinst> `abort-remove'
#        * <deconfigured's-postinst> `abort-deconfigure' `in-favour'
#          <failed-install-package> <version> `removing'
#          <conflicting-package> <version>
# for details, see http://www.debian.org/doc/debian-policy/ or
# the debian-policy package


case "$1" in
    configure)
	setup_rpkid_group
	setup_rpkid_user
	setup_apache
	setup_django
	setup_cron
    ;;

    abort-upgrade|abort-remove|abort-deconfigure)
    ;;

    *)
        echo "postinst called with unknown argument \\`$1'" >&2
        exit 1
    ;;
esac

# dh_installdeb will replace this with shell code automatically
# generated by other debhelper scripts.

#DEBHELPER#

exit 0
''')

with open('debian/rpki-ca.upstart', "wb") as f:
  f.write('''\
# RPKI CA Service

description     "RPKI CA Servers"
author		"Rob Austein <sra@hactrn.net>"

# This is almost certainly wrong.  Suggestions on how to improve this
# welcome, but please first read the Python code to understand what it
# is doing.

# Our only real dependencies are on mysqld and our config file.

start on started mysql
stop on stopping mysql

pre-start script
    if  test -f /etc/rpki.conf &&
	test -f /usr/share/rpki/ca.cer &&
	test -f /usr/share/rpki/irbe.cer &&
	test -f /usr/share/rpki/irdbd.cer &&
	test -f /usr/share/rpki/rpkid.cer &&
	test -f /usr/share/rpki/rpkid.key
    then
        install -m 755 -o rpkid -g rpkid -d /var/run/rpki /usr/share/rpki/publication

	# This should be running as user rpkid, but I haven't got all
	# the pesky details worked out yet.  Most testing to date has
	# either been all under a single non-root user or everything
	# as root, so, eg, running "rpkic initialize" as root will not
	# leave things in a sane state for rpkid running as user
	# rpkid.
	#
	# In the interest of debugging the rest of this before trying
	# to break new ground, run daemons as root for the moment,
	# with the intention of coming back to fix this later.
	#
	#sudo -u rpkid /usr/sbin/rpki-start-servers
	/usr/sbin/rpki-start-servers

    else
	stop
	exit 0
    fi
end script

post-stop script
    for i in rpkid pubd irdbd rootd
    do
	if test -f /var/run/rpki/$i.pid
	then
	    kill `cat /var/run/rpki/$i.pid`
	fi
    done
end script
''')

with open('debian/rpki-rp.install', "wb") as f:
  f.write('''\
etc/rcynic.conf
etc/rpki/trust-anchors
etc/xinetd.d/rpki-rtr
usr/bin
var/rcynic
''')

with open('debian/rpki-rp.lintian-overrides', "wb") as f:
  f.write('''\
# The RPKI code requires a copy of the OpenSSL library with both the
# CMS code and RFC 3779 code enabled.  All recent versions of OpenSSL
# include this code, but it's not enabled on all platforms.  On Ubuntu
# 12.04 LTS, the RFC 3779 code is disabled.  So we take the least bad
# of our several bad options, and carefully link against a private
# copy of the OpenSSL crypto library built with the options we need,
# with all the voodoo necessary to avoid conflicts with, eg, the
# OpenSSL shared libraries that are already linked into Python.
#
# It would be totally awesome if the OpenSSL package maintainers were
# to enable the RFC 3779 code for us, but I'm not holding my breath.
#
# In the meantime, we need to tell lintian to allow this nasty hack.

rpki-rp: embedded-library

# /var/rcynic is where we have been keeping this for years.  We could change
# but all the documentation says /var/rcynic.  Maybe some day we will
# figure out a politically correct place to put this, for now stick
# with what the documentation leads the user to expect.

rpki-rp: non-standard-dir-in-var
''')

with open('debian/rpki-rp.postinst', "wb") as f:
  f.write('''\
#!/bin/sh
# postinst script for rpki-rp
#
# see: dh_installdeb(1)

set -e

setup_rcynic_ownership() {
    install -o rcynic -g rcynic -d /var/rcynic/data /var/rcynic/rpki-rtr /var/rcynic/rpki-rtr
    if test -d /var/www
    then
	install -o rcynic -g rcynic -d /var/www/rcynic
    fi
}

setup_rcynic_user() {
    if ! getent passwd rcynic >/dev/null
    then
	useradd -g rcynic -M -N -d /var/rcynic -s /sbin/nologin -c "RPKI validation system" rcynic
    fi
}

setup_rcynic_group() {
    if ! getent group rcynic >/dev/null
    then
	groupadd rcynic
    fi
}

# We want to pick a *random* minute for rcynic to run, to spread load
# on repositories, which is why we don't just use a package crontab.

setup_rcynic_cron() {
    crontab -l -u rcynic 2>/dev/null |
    awk -v t=`hexdump -n 2 -e '"%u\\n"' /dev/urandom` '
        BEGIN { cmd = "exec /usr/bin/rcynic-cron" }
	$0 !~ cmd { print }
	END { printf "%u * * * *\\t%s\\n", t % 60, cmd }
    ' |
    crontab -u rcynic -
}

setup_rpki_rtr_listener() {
    killall -HUP xinetd
}

# summary of how this script can be called:
#        * <postinst> `configure' <most-recently-configured-version>
#        * <old-postinst> `abort-upgrade' <new version>
#        * <conflictor's-postinst> `abort-remove' `in-favour' <package>
#          <new-version>
#        * <postinst> `abort-remove'
#        * <deconfigured's-postinst> `abort-deconfigure' `in-favour'
#          <failed-install-package> <version> `removing'
#          <conflicting-package> <version>
# for details, see http://www.debian.org/doc/debian-policy/ or
# the debian-policy package


case "$1" in
    configure)
	setup_rcynic_group
	setup_rcynic_user
	setup_rcynic_ownership
	setup_rcynic_cron
	setup_rpki_rtr_listener
    ;;

    abort-upgrade|abort-remove|abort-deconfigure)
    ;;

    *)
        echo "postinst called with unknown argument \\`$1'" >&2
        exit 1
    ;;
esac

# dh_installdeb will replace this with shell code automatically
# generated by other debhelper scripts.

#DEBHELPER#

exit 0
''')

with open('debian/rpki-rp.prerm', "wb") as f:
  f.write('''\
#!/bin/sh
# prerm script for rpki-rp
#
# see: dh_installdeb(1)

set -e

# summary of how this script can be called:
#        * <prerm> `remove'
#        * <old-prerm> `upgrade' <new-version>
#        * <new-prerm> `failed-upgrade' <old-version>
#        * <conflictor's-prerm> `remove' `in-favour' <package> <new-version>
#        * <deconfigured's-prerm> `deconfigure' `in-favour'
#          <package-being-installed> <version> `removing'
#          <conflicting-package> <version>
# for details, see http://www.debian.org/doc/debian-policy/ or
# the debian-policy package


case "$1" in
    remove)

	crontab -l -u rcynic 2>/dev/null | awk '
	    $0 !~ "exec /usr/bin/rcynic-cron" {
		line[++n] = $0;
	    }
	    END {
		if (n)
		    for (i = 1; i <= n; i++)
			print line[i] | "crontab -u rcynic -";
		else
		    system("crontab -u rcynic -r");
	    }'
	;;

    upgrade|deconfigure)
    ;;

    failed-upgrade)
    ;;

    *)
        echo "prerm called with unknown argument \\`$1'" >&2
        exit 1
    ;;
esac

# dh_installdeb will replace this with shell code automatically
# generated by other debhelper scripts.

#DEBHELPER#

exit 0
''')

with open('debian/rules', "wb") as f:
  f.write('''\
#!/usr/bin/make -f
# -*- makefile -*-

# Uncomment this to turn on verbose mode.
export DH_VERBOSE=1

%:
	dh $@ --with python2

override_dh_auto_configure:
	dh_auto_configure -- --disable-target-installation --enable-python-install-layout=deb

override_dh_auto_test:
	@true
''')

os.makedirs('debian/source')

with open('debian/source/format', "wb") as f:
  f.write('''\
3.0 (native)
''')
