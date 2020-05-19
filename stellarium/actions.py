#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.export("CFLAGS", get.CFLAGS())
	shelltools.export("CXXFLAGS", get.CXXFLAGS())
	cmaketools.configure("-DENABLE_GPS=0")

def build():
	cmaketools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("BACKERS.md", "ChangeLog", "CONTRIBUTING.md", "COPYING", "CREDITS.md", "README.md")

