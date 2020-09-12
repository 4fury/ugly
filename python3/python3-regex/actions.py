#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

i = "-Wno-maybe-initialized \
     -Wno-unused-but-set-variable \
    "

def setup():
	pisitools.cflags.add(i)

def build():
	pythonmodules.compile(pyVer = "3")

def install():
	pythonmodules.install(pyVer = "3")

	pisitools.dodoc("PKG-INFO", "README.rst")

