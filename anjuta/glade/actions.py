#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

shelltools.export("PYTHON", "/usr/bin/python3")

j = "-Dgladeui=true \
     -Dpython=true \
     -Dwebkit2gtk=false \
     -Dgjs=false \
    "

def setup():
#	shelltools.system("sed -i 's|AX_CHECK|#AX_CHECK|' configure")
	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README.md", "TODO")

