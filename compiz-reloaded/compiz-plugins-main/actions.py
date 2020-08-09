#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

#from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
#	shelltools.system("./autogen.sh --prefix=/usr --disable-static")
	pisitools.dosed("configure", "gtk-update-icon-cache", "gtk3-update-icon-cache")
	autotools.configure("--disable-silent-rules --disable-static")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING")
