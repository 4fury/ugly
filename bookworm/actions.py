#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	mesontools.configure()

def build():
	mesontools.make()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "CODE_OF_CONDUCT.md", "COPYING", "README.md")

