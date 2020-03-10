#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools

def build():
	pythonmodules.compile(parameters = "--prefix=/usr")

def install():
	pythonmodules.install(parameters = "--prefix=/usr")

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS")

