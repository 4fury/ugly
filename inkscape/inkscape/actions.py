#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-DCMAKE_INSTALL_PREFIX=/usr \
     -DCMAKE_INSTALL_LIBDIR=lib \
     -DCMAKE_BUILD_TYPE=Release \
     -DWITH_IMAGE_MAGICK=OFF \
     -DBUILD_STATIC_LIBS=OFF \
     -DBUILD_SHARED_LIBS=ON \
     -DBUILD_TESTING=OFF -L \
    "

shelltools.export("PYTHON", "/usr/bin/python3")
shelltools.system("find share/extensions -iname '*.py' -exec sed -i 's|env\ python$|env python3|g' {} \;")

def setup():
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure(j, sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	shelltools.cd("..")
	pisitools.dodoc("AUTHORS", "CONTRIBUTING.md", "COPYING", "NEWS.md", "README.md", "TRANSLATORS")

