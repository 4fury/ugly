#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
	pythonmodules.compile(pyVer = '3')

def check():
#	pythonmodules.run("test_css.py", pyVer = '3')
#	pythonmodules.run("test_scour.py", pyVer = '3')

def install():
	pythonmodules.install(pyVer = '3')

	pisitools.dodoc("HISTORY.md", "README.md")

