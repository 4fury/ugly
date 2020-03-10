#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
#from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("meson . build --prefix=/usr -Dplugin_git=false -Dplugin_devhelp=false -Dplugin_flatpak=false")
#	mesontools.configure()

def build():
	shelltools.system("ninja -C build")
#	mesontools.make()

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())
#	mesontools.install()

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README.md")

