#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "WXCONFIG=/usr/bin/wx-config-gtk3 -fopenmp"

def build():
	shelltools.export("CXXFLAGS", get.CXXFLAGS())
	shelltools.export("CFLAGS", get.CFLAGS())
	autotools.make("PREFIX=/usr %s" % j)

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("README.md", "docs/Change.log")

