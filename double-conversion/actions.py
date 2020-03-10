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
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure("\
	\
	-DBUILD_SHARED_LIBS=ON \
	\
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_LIBDIR=lib \
	-DCMAKE_INSTALL_PREFIX=/usr", sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.install()

	shelltools.cd("..")
	pisitools.dodoc("AUTHORS", "Changelog", "COPYING", "LICENSE", "README.md")

