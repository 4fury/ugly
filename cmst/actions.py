#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

def setup():
	shelltools.system("sed -i '/^conf.path =/c conf.path = /usr/share/dbus-1/system.d' apps/rootapp/rootapp.pro")
	qt5.configure()

def build():
	qt5.make()

def install():
	qt5.install()

	pisitools.dodoc("README.md")

