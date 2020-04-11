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
	cmaketools.configure("-DCMAKE_INSTALL_PREFIX=/usr -DCMAKE_BUILD_TYPE=Release \
	\
	-DWITH_IMAGE_MAGICK=OFF -DBUILD_TESTING=OFF", sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	shelltools.cd("..")
	pisitools.dodoc("AUTHORS", "CONTRIBUTING.md", "COPYING", "NEWS.md", "README.md", "TRANSLATORS")

