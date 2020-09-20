#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import qt5
from pisi.actionsapi import get

f = "-Wno-deprecated-declarations -Wno-implicit-fallthrough -Wno-unused-result"

def setup():
	qt5.configure(parameters = "QMAKE_CXXFLAGS+='%s'" % f)

def build():
	qt5.make()

def install():
	qt5.install()

