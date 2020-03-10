#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.export("PYTHON", "/usr/bin/python3")

	shelltools.export("CFLAGS", \
	"%s -Wno-deprecated-declarations \
	-Wno-unused-variable \
	-Wno-pointer-compare \
	-Wno-unused-function" % get.CFLAGS())

	autotools.configure("\
	\
	--enable-gladeui \
	--enable-python \
	--enable-introspection --disable-webkit2gtk")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "NEWS", "README", "TODO")

