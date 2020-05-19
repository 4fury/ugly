#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--enable-lua \
     --enable-animation \
     --disable-schemas \
     --disable-deprecated \
     --with-system-lua \
    "

z = "-Wno-int-conversion \
     -Wno-pointer-to-int-cast \
     -Wno-int-to-pointer-cast \
     -Wno-implicit-function-declaration \
    "

def setup():
	pisitools.cflags.add(z)
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("ChangeLog", "COPYING", "NEWS", "README")

