#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import qt5

w = "-Wno-deprecated -Wno-deprecated-declarations"

def setup():
    qt5.configure(parameters = "QMAKE_CXXFLAGS='%s'" % w)

def build():
    qt5.make()

def install():
    qt5.install()

    pisitools.dodoc("LICENSE", "LISANS", "OKUBUNU", "README", "Lizenz")

