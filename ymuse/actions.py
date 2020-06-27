#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
#	shelltools.system("find . -type f -regex '.*\(go\|glade\)' -exec sed -i 's/ymuse-//g' {} \;")
	shelltools.system("go generate -v")

def build():
	shelltools.system("go build -v")

def install():
	pisitools.dobin("ymuse")
	pisitools.insinto("/usr/share/applications", "resources/ymuse.desktop", "ymuse.desktop")
	shelltools.copy("resources/icons", "%s/%s/icons" % (get.installDIR(), get.dataDIR()))
	for i in shelltools.ls("resources/i18n/generated/*/LC_MESSAGES/ymuse.mo"):
		pisitools.domo(i)

	pisitools.dodoc("COPYING", "README.md")

