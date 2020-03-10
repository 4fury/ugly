#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

options = "\
          --freedom=partial \
          --without-info \
          --dest-dir=%s \
          " % get.installDIR()

def install():
	pythonmodules.run("setup.py install %s" % options, pyVer = "3")
	pisitools.removeDir("var")

	pisitools.dodoc("CHANGELOG", "CONTRIBUTING", "README.md")

