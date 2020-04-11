#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

options = " --disable-root-passwd --with-motif --with-pam --with-xshm-ext \
--with-xdbe-ext --with-dpms-ext --without-gtk --without-systemd"

def setup():
#	shelltools.system("sed -i '502,513d' driver/Makefile.in")
#	shelltools.system("sed -i '/LINGUAS/s/sv\ vi/sv tr vi/' configure.in")
#	autotools.autoreconf("-fi")
	autotools.configure("--mandir=%s" % get.installDIR()
	+ "/usr/man --infodir=%s" % get.installDIR() + "/usr/share/info --sysconfdir=%s" % get.installDIR()
	+ "/etc --datadir=%s" % get.installDIR() + "/usr/share --libexecdir=%s" % get.installDIR()
	+ "/usr/libexec --with-x-app-defaults=%s" % get.installDIR() + "/usr/share/X11/app-defaults --datarootdir=%s"
	% get.installDIR() + "/usr --bindir=%s" % get.installDIR() + "/usr/bin" + options)

def build():
	autotools.make()

def install():
#	shelltools.makedirs("%s/usr/share/applications" % get.installDIR())
#	autotools.make("install")
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.insinto("/usr/share/applications", "driver/screensaver-properties.desktop", "screensaver-properties.desktop")
#	shelltools.system("mkdir " + get.installDIR() + "/usr/share/applications")
#	shelltools.system("cp %s" % get.workDIR() + "/xscreensaver-5.43/driver/screensaver-properties.desktop " + get.installDIR() + "/usr/share/applications/xscreensaver-properties.desktop")
#	shelltools.system("rm /usr/share/applications/xscreensaver-properties.desktop")

	pisitools.dodoc("README*")

