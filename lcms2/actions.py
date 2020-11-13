#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "--disable-dependency-tracking \
     --disable-static \
     --with-jpeg \
     --with-tiff \
     --with-zlib \
     --libdir=/usr/lib%s \
    " % ("32" if get.buildTYPE() == "emul32" else "" )

def setup():
	autotools.configure(i)

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "README.1ST")

