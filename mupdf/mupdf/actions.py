#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "-Wno-maybe-uninitialized \
     -Wno-unused-but-set-variable \
     -Wno-unused-result \
    "

j = "USE_SYSTEM_LIBS=yes prefix=/usr"

t = "freetype, \
     harfbuzz, \
     jbig2dec, \
     libjpeg, \
     openjpeg, \
     zlib, \
     glut, \
     curl, \
    "

def build():
	pisitools.cflags.add(i)
	shelltools.system("rm -rf thirdparty/{%s}" % t)
	shelltools.system("sed '/TOFU_CJK /c #define TOFU_CJK 1/' -i include/mupdf/fitz/config.h")
	shelltools.system("sed -i '/ttc/s/^/#/' Makefile")
	autotools.make(j)

def install():
	autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), j))

	pisitools.dodoc("CHANGES", "README", "COPYING")

