#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

WorkDir = "ff0a801413e612f74fe4c5d251e4bf36c6628013"

t = "--prefix=/usr \
     --mandir=/usr/share/man \
     gtk2 jp2 man gtk3 tiff lcms2 jpeg webp GIF imagick cflags \
    "

def setup():
	autotools.configure(t)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("COPYING", "NEWS", "README")

