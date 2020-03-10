#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pisitools
from pisi.actionsapi import get
import fnmatch
import os

def setup():
	pisitools.dosed("clamtk", "use ClamTk::Prefs", "use lib \"/usr/lib/\";\nuse ClamTk::Prefs")
	pisitools.dosed("clamtk", "use ClamTk::GUI", "use lib \"/usr/lib/\";\nuse ClamTk::GUI")
	pisitools.dosed("clamtk", "use ClamTk::Analysis", "use lib \"/usr/lib/\";\nuse ClamTk::Analysis")

def install():
	pisitools.dobin("clamtk")
	pisitools.dolib("lib/*", "/usr/lib/perl5/vendor_perl/"+ get.curPERL()+ "/ClamTk")
	pisitools.doman("clamtk.1.gz")
	pisitools.insinto("/usr/share/applications", "clamtk.desktop")
	pisitools.insinto("/usr/share/pixmaps", "images/clamtk.png")
	pisitools.insinto("/usr/share/pixmaps", "images/clamtk.xpm")
	#pisitools.insinto("/usr/lib/perl5/vendor_perl/5.20.0/ClamTk", "lib/*.pm")
	pisitools.dodoc("CHANGES", "DISCLAIMER", "LICENSE", "README.md")

	#Locales
	for i in os.listdir("po"):
		if fnmatch.fnmatch(i, '*.po'):
			pisitools.domo("po/" + i, i.replace(".po", ""), "clamtk.mo")

