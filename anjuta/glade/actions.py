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

w = "-Wno-deprecated-declarations \
     -Wno-pointer-compare \
     -Wno-unused-variable \
     -Wno-unused-function \
    "

def setup():
	pisitools.cflags.add(w)
#	autotools.autoreconf("-fi")
#	shelltools.system("sed -i 's|AX_CHECK|#AX_CHECK|' configure")
	autotools.configure("--enable-python --enable-gladeui")

	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README")

