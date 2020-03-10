# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools

def setup():
	cmaketools.configure()

def build():
	cmaketools.make()

def install():
	cmaketools.install()

	pisitools.dodoc("CHANGELOG", "INSTALL.md", "LICENSE", "README.md", "xstarter.conf")

