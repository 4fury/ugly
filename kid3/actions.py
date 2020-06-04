#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import kde5

j = "-DCMAKE_INSTALL_PREFIX=/usr \
     -DCMAKE_BUILD_TYPE=Release \
     -DWITH_GSTREAMER=ON \
     -DWITH_MP4V2=ON \
     -DWITH_FFMPEG=ON \
     -DBUILD_TESTING=OFF \
    "

def setup():
	shelltools.export("DOCBOOKDIR", "/usr/share/xml/docbook/xsl-stylesheets")
	kde5.configure(j)

def build():
	kde5.make()

def install():
	kde5.install()

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING*", "README")

