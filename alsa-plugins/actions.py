#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

if "_" in get.srcVERSION():
	WorkDir = get.srcNAME()

def setup():
	autotools.autoreconf("-fi")
	autotools.configure("--disable-static --with-speex=lib")

	pisitools.dosed("libtool", " -shared ", " -Wl,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("COPYING*", "doc/*.txt", "doc/README*")

