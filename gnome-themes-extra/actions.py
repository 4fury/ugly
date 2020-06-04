#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--prefix=/usr \
     --disable-gtk3-engine \
    "

def setup():
	shelltools.system("./autogen.sh %s" % j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.removeDir("/usr/share/locale")
	pisitools.dodoc("LICENSE", "NEWS", "README.md")

