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
shelltools.export("LC_ALL", "C")

f = "-Wno-deprecated-declarations \
     -Wno-format-y2k \
     -Wno-discarded-qualifiers \
     -Wno-enum-compare \
     -Wno-format-nonliteral \
     -Wno-unused-variable \
     -Wno-maybe-uninitialized \
     -Wno-incompatible-pointer-types \
     -Wno-unused-but-set-variable \
     -Wno-pointer-compare \
     -Wno-strict-prototypes \
     -Wno-unused-value \
     -Wno-unused-function \
     -Wno-write-strings \
     -Wno-unused-result \
     -Wno-pointer-sign \
     -Wno-pedantic \
     -Wno-cpp \
    "

w = "--enable-plugin-terminal \
     --enable-plugin-devhelp \
     --enable-glade-catalog \
     --enable-introspection \
     --enable-plugin-glade \
     --enable-packagekit \
     --disable-schemas-compile \
     --disable-gtk-doc \
     --disable-static \
    "

def setup():
	pisitools.cflags.add(f)
	autotools.configure(w)

	pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "THANKS")

