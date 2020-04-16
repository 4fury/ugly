#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
	shelltools.cd("src")
	for t in ["*.c"]:
		shelltools.system("gcc -D LINUX  -o ../pwall %s -I. -g -lm `pkg-config --libs --cflags gtk+-3.0`" % t)

def install():
	pisitools.dobin("pwall")

