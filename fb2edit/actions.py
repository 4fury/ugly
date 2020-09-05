#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5
from pisi.actionsapi import get

def setup():
	qt5.configure()
#	cmaketools.configure()

def build():
	qt5.make()
#	cmaketools.make()

def install():
	qt5.install()
#	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

#	pisitools.dodoc("AUTHORS")

