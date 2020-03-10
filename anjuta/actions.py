#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

#from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	pisitools.cflags.add("-Wno-deprecated-declarations")
#	shelltools.export("PYTHON", "/usr/bin/python3")
	autotools.configure("\
	\
	--enable-plugin-terminal --enable-introspection \
	\
	--disable-schemas-compile \
	--disable-plugin-devhelp \
	--disable-gtk-doc --disable-static")

	pisitools.dosed("libtool"," -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "THANKS")

