#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import get
from pisi.actionsapi import pisitools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools

def setup():
    shelltools.export("FORCE_SOURCE_DATE", "1")
    cmaketools.configure("-DCMAKE_INSTALL_LIBDIR=lib \
                          -DCMAKE_BUILD_TYPE=Release \
                          -DCMAKE_EXE_LINKER_FLAGS=-lm")

def build():
    cmaketools.make()

def install():
    cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

    #pisitools.dodoc("README*", "COPYING*")