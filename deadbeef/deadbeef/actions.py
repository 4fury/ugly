#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-Wno-deprecated-declarations \
     -Wno-multichar \
     -Wno-parentheses \
     -Wno-unused-value \
     -Wno-unused-result \
     -Wno-dangling-else \
     -Wno-unused-variable \
     -Wno-stringop-overflow \
     -Wno-misleading-indentation \
     -Wno-unused-but-set-variable \
     -Wno-incompatible-pointer-types \
    "

def setup():
    shelltools.export("CC", "clang")
    shelltools.export("CXX", "clang++")
#    pisitools.cflags.add(j)
#    pisitools.cxxflags.add("-Wno-deprecated-declarations -Wno-vla")

#    autotools.autoreconf("-fiv")
    autotools.configure("--disable-oss")

#    pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
    autotools.make()

def install():
    autotools.rawInstall("DESTDIR=%s" % get.installDIR())

    pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README")

