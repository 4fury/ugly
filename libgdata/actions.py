#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools

j = "-Dgnome=disabled \
     -Dgoa=disabled \
     -Dgtk3=disabled \
     -Doauth1=disabled \
     -Dalways_build_tests=false \
     -Dinstalled_tests=false \
     -Dgtk_doc=false \
"

def setup():
	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README")

