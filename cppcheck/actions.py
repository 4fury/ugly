#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("PYTHON", "/usr/bin/python3")

i = 'FILESDIR=/usr/share/cppcheck CFGDIR=cfg'

f = '-Wno-multichar -Wno-sign-compare -Wno-unused-function -Wno-maybe-uninitialized \
-Wno-implicit-fallthrough -Wno-deprecated-declarations'

def setup():
	pisitools.cxxflags.add("-DNDEBUG -DNEW_Z3=1 %s" % f)
	cmaketools.configure("-DCLANG_TIDY_ENABLED=OFF -DWITH_GUI=ON -L")

def build():
	cmaketools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("")

