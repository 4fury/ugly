#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

i = "PREFIX=/usr TARGET=gtk3"

def build():
	autotools.make(i)

def install():
	autotools.rawInstall("DESTDIR=%s %s" % (get.installDIR(), i))

	pisitools.dodoc("ChangeLog.md", "README.md")

