#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

t = "%s/usr/bin" % get.installDIR()

def setup():
	pisitools.dosed("build-aux/meson/postinstall.py", "gtk", "gtk3")
	mesontools.configure("--prefix=/usr")

def build():
	mesontools.build()

def install():
	mesontools.install()
	pisitools.dosym("%s/com.github.johnfactotum.Foliate" % t, "%s/foliate" % t)

	pisitools.dodoc("COPYING", "README.md")

