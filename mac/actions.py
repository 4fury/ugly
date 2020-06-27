#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

jobs = get.makeJOBS().replace("-j5", "-j1")
#WorkDir = "Source"

def setup():
#	pisitools.dosym("../Source/Projects/NonWindows/Makefile", "Makefile")
	shelltools.system("ln -s ../Source/Projects/NonWindows/Makefile ./")
#	autotools.configure()

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

#	pisitools.dodoc("")

