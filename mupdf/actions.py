#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def build():
    # remove bundled packages, use our system libraries
    shelltools.system("rm -rf thirdparty/{curl,freeglut,harfbuzz,libjpeg,openjpeg,zlib}")
    pisitools.ldflags.add("-lglut")
    pisitools.cflags.add("-lglut -Wno-maybe-uninitialized -Wno-unused-but-set-variable -Wno-unused-result")
    shelltools.system("sed '/TOFU_CJK /c #define TOFU_CJK 1/' -i include/mupdf/fitz/config.h")
    shelltools.system("sed -i '/ttc/s/^/#/' Makefile")
    autotools.make("USE_SYSTEM_LIBS=yes USE_SYSTEM_FREETYPE=no USE_SYSTEM_JBIG2DEC=no prefix=/usr")

    # remove bundled packages, use our system libraries
    #shelltools.system("rm -rf thirdparty/{curl,freeglut,freetype,harfbuzz,libjpeg,openjpeg,zlib}")

def install():
    autotools.rawInstall("DESTDIR=%s USE_SYSTEM_LIBS=yes prefix=/usr" % get.installDIR())
    #pisitools.removeDir("/usr/lib")

    pisitools.dodoc("CHANGES", "README", "COPYING")
