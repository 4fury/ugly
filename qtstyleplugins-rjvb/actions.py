#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

#flg = "-Wno-deprecated-declarations -Wno-implicit-fallthrough -Wno-unused-result"
j = "-DENABLE_KDE=ON \
     -DENABLE_KFUSION=ON \
     -DENABLE_CLEANLOOKS=ON \
     -DENABLE_PLASTIQUE=ON \
     -DENABLE_GTK2=ON \
     -DENABLE_GTK3=OFF \
    "

def setup():
#	qt5.configure(parameters = "QMAKE_CXXFLAGS+='%s'" % flg)
	cmaketools.configure("%s -L" % j)

def build():
	cmaketools.make()

def install():
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("README.md")

