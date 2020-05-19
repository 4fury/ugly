#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import get

def setup():
	for z in ["src/sk1.*"]:
		shelltools.chmod(z, mode = 0644)
	shelltools.export("CFLAGS", get.CFLAGS())

def build():
	pythonmodules.compile()

def install():
	pythonmodules.install()

