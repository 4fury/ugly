#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("PYTHON", "/usr/bin/python3")

flags = "-Wno-deprecated-declarations \
-Wno-unused-variable -Wno-pointer-compare \
-Wno-unused-function"

def setup():
	pisitools.cflags.add(flags)
	autotools.autoreconf("-fi")
	shelltools.system("sed -i 's|AX_CHECK|#AX_CHECK|' configure")
	autotools.configure("--enable-python --enable-gladeui")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

