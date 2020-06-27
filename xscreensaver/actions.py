#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--with-gl \
     --with-gtk \
     --with-xft \
     --with-pam \
     --with-shadow \
     --with-dpms-ext \
     --with-xshm-ext \
     --with-xdbe-ext \
     --without-systemd \
    "

shelltools.export("GTK_DATADIR", "%s/usr/share" % get.installDIR())

def setup():
#	autotools.configure(j)
	autotools.configure("--mandir=%s" % get.installDIR()
	+ "/usr/man --infodir=%s" % get.installDIR() + "/usr/share/info --sysconfdir=%s" % get.installDIR()
	+ "/etc --datadir=%s" % get.installDIR() + "/usr/share --libexecdir=%s" % get.installDIR()
	+ "/usr/libexec --with-x-app-defaults=%s" % get.installDIR() + "/usr/share/X11/app-defaults --datarootdir=%s"
	% get.installDIR() + "/usr --bindir=%s" % get.installDIR() + "/usr/bin")

def build():
	autotools.make()

def install():
	shelltools.export("GTK_DATADIR", "%s/usr/share" % get.installDIR())
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

#Working around unbudging shortcut directory issue, please disable sandboxing
#	shelltools.system("mkdir " + get.installDIR() + "/usr/share/applications")
#	shelltools.system("cp %s" % get.workDIR() + "/xscreensaver-5.44/driver/screensaver-properties.desktop " + get.installDIR() + "/usr/share/applications/xscreensaver-properties.desktop")
#	shelltools.system("rm /usr/share/applications/xscreensaver-properties.desktop")

	pisitools.dodoc("INSTALL", "README", "README.hacking", "README.VMS")

