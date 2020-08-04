#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_BUILD_TYPE=Release \
     -DCMAKE_CXX_STANDARD="11" \
     -DENABLE_LIBINDICATE=OFF \
     -DwxWidgets_CONFIG_EXECUTABLE=/usr/bin/wx-config-gtk3 \
     -DwxWidgets_wxrc_EXECUTABLE=/usr/bin/wxrc-3.0 \
     -DwxWidgets_INCLUDE_DIRS=/usr/include/wx-3.0 \
     -DCMAKE_EXE_LINKER_FLAGS=-lwx_gtk3u_aui-3.0 -L \
    "

t = "build-guayadeque"

def setup():
	shelltools.makedirs(t)
	shelltools.cd(t)
	cmaketools.configure(j, sourceDir = '..')

def build():
	shelltools.cd(t)
	cmaketools.make()

def install():
	shelltools.cd(t)
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

#	pisitools.dodoc("ChangeLog", "LICENSE", "README")

