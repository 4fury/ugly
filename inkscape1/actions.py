#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("sed -i '16a#include <cstring>' src/extension/prefdialog/widget.h")
	shelltools.system("sed -i '525a\ \ \ \ /*' src/inkscape-application.cpp")
	shelltools.system("sed -i '534a\ \ \ \ */' src/inkscape-application.cpp")

	shelltools.system("sed -i '66a\ \ \ \ /*' src/inkview-application.cpp")
	shelltools.system("sed -i '69a\ \ \ \ */' src/inkview-application.cpp")

	shelltools.system("sed -i 's/python/python3/g' CMakeScripts/Dist.cmake")
	shelltools.system("find . -iname 'CMakeLists.txt' -exec sed -i 's/python/python3/g' {} \;")

	shelltools.makedirs("build")

	shelltools.cd("build")
	cmaketools.configure("\
	\
	-DWITH_DBUS=OFF \
	-DWITH_PROFILING=OFF \
	\
	-DCMAKE_BUILD_TYPE=Debug \
	-DCMAKE_INSTALL_PREFIX=/usr", sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.install()

	shelltools.cd("..")
	pisitools.dodoc("AUTHORS", "CONTRIBUTING.md", "COPYING", "INSTALL.md", "NEWS.md", "README.md", "TRANSLATORS")

