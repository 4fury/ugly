#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get
from pisi.actionsapi import qt5

t = 'FILESDIR=/usr/share/cppcheck CFGDIR=/usr/share/cppcheck/cfg'

z = "-DNDEBUG \
     -Wall \
     -Wno-missing-field-initializers \
     -Wno-multichar \
     -Wno-sign-compare \
     -Wno-unused-function \
     -Wno-implicit-fallthrough \
     -Wno-maybe-uninitialized \
     -Wno-deprecated-declarations \
    "

def build():
	pisitools.cxxflags.add(z)
	autotools.make("MATCHCOMPILER=yes %s HAVE_RULES=yes HAVE_QCHARTS=yes USE_Z3=no" % t)

	shelltools.cd("gui")
	qt5.configure()
	qt5.make()

def check():
	autotools.make("check %s" % t)

def install():
	pisitools.dobin("gui/cppcheck-gui")
	pisitools.insinto("/usr/share/applications", "gui/cppcheck-gui.desktop", "cppcheck-gui.desktop")
	pisitools.insinto("/usr/share/pixmaps", "gui/cppcheck-gui.svg", "cppcheck-gui.svg")
	pisitools.insinto("/usr/share/pixmaps", "gui/cppcheck-gui.png", "cppcheck-gui.png")

	autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), t))

	pisitools.dodoc("AUTHORS", "COPYING", "readme*")

