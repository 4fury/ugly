#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 2.
# See the file http://www.gnu.org/copyleft/gpl.txt.

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "yaru-20.04.6"
w = "--prefix=/usr \
     -Dicons=false \
     -Dgnome-shell=false \
     -Dgnome-shell-gresource=false \
     -Dsounds=false \
     -Dsessions=false \
    "

def setup():
	shelltools.system("meson . build %s" % w)

def build():
	shelltools.system("ninja -C build")

def install():
	shelltools.system("DESTDIR=%s ninja -C build install" % get.installDIR())

