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
shelltools.export("JAVA_HOME", "/usr/lib/jvm/java-8-openjdk")
shelltools.export("JOBS", get.makeJOBS().replace("-j5", "-j1"))

f = "-Wno-deprecated-declarations \
     -Wno-address \
     -Wno-incompatible-pointer-types \
     -Wno-unused-variable \
     -Wno-unused-result \
     -Wno-cpp \
     -Wno-implicit-function-declaration \
     -Wno-int-to-pointer-cast \
     -Wno-unused-but-set-variable \
     -Wno-maybe-uninitialized \
     -Wno-unused-function \
    "

w = "--enable-system-sqlite \
     --with-java=yes \
     --with-ldap=no \
    "

def setup():
	pisitools.cflags.add(f)
	autotools.configure(w)

	pisitools.dosed("libtool", " -shared ", " -Wl,-O1--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

