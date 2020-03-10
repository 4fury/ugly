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
	shelltools.export("JAVA_HOME", "/usr/lib/jvm/java-8-openjdk")
	shelltools.export("PYTHON", "/usr/bin/python3")
	autotools.configure("\
	\
	--enable-system-sqlite \
	--enable-json \
	--with-java=yes \
	--with-graphviz \
	--with-ui=no \
	--with-ldap=no")

	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "NEWS", "README")

