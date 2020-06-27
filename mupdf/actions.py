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

def build():
	pisitools.cflags.add(i)
	shelltools.system("sed '/TOFU_CJK /c #define TOFU_CJK 1/' -i include/mupdf/fitz/config.h")
	shelltools.system("sed -i '/ttc/s/^/#/' Makefile")
	autotools.make("USE_SYSTEM_LIBS=no prefix=/usr")

def install():
	autotools.rawInstall("DESTDIR=%s USE_SYSTEM_LIBS=no prefix=/usr" % get.installDIR())

	pisitools.dodoc("CHANGES", "README", "COPYING")

