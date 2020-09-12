#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_INSTALL_LIBDIR=lib \
     -DBUILD_SHARED_LIBS=ON \
     -DGLFW_USE_OSMESA=ON \
    "

def build():
	cmaketools.configure(j)

def install():
	cmaketools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("LICENSE.md", "README.md")

