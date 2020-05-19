#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("PYTHON", "/usr/bin/python3")

def setup():
	pisitools.ldflags.add("-lz")
	pisitools.cxxflags.add("-lz")
	cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_INSTALL_LIBDIR=lib")
#	autotools.configure("--disable-static --enable-sdl --with-zlib")

def build():
	cmaketools.make("-j1")
#	autotools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())
#	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

#	pisitools.dohtml("docs/*.htm*")
	pisitools.dodoc("ChangeLog", "COPYING.LIB", "README", "TODO", "docs/COPYING*", "docs/README.SDL")

