#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def install():
	shelltools.cd("..")
	shelltools.system("find . -type d -exec chmod 755 {} \;")
	shelltools.system("find . -type f -exec chmod 644 {} \;")

	pisitools.dodir("/usr/share/themes")
	for t in shelltools.ls("ClassicLooks*"):
		shelltools.system("cp -rp '%s' %s/usr/share/themes" % (t, get.installDIR()))

	pisitools.dodoc("HISTORY", "README")

