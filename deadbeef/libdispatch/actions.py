#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_INSTALL_PREFIX=/usr \
     -DBlocksRuntime_INCLUDE_DIR=/usr/include \
     -DBlocksRuntime_LIBRARIES=/usr/lib/clang/10.0.0/lib/linux/libBlocksRuntime.so \
     -DBUILD_TESTING=OFF \
    "

def setup():
	shelltools.export("CC", "clang")
	shelltools.export("CXX", "clang++")
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure(j, sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("../AUTHORS")

