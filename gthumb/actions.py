#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
#from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.system("unset LC_ALL")

z = "-Dwarn-deprecated=false \
     -Dclutter=false \
     -Dlibbrasero=false \
    "

def setup():
#	mesontools.configure(z)
	shelltools.system("meson --prefix=/usr %s . build" % z)

def build():
#	mesontools.build()
	shelltools.system("ninja -C build")

def install():
#	mesontools.install()
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "MAINTAINERS", "NEWS", "README.md")

