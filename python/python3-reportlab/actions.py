#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

j = "-Wno-unused-but-set-variable \
     -Wno-unused-function \
     -Wno-misleading-indentation \
     -Wno-maybe-uninitialized \
     -Wno-strict-prototypes \
     -Wno-incompatible-pointer-types \
     -Wno-strict-aliasing \
     -Wno-pointer-sign \
     -Wno-format \
    "

def build():
	pisitools.cflags.add(j)
	pythonmodules.compile(pyVer = '3')

def install():
	pythonmodules.install(pyVer = '3')

	pisitools.dodoc("CHANGES.md", "LICENSE.txt", "README.txt")

