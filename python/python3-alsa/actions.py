#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import pythonmodules
#from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools
#from pisi.actionsapi import get

#WorkDir = "pyalsaaudio-%s" % get.srcVERSION()
#examples = "%s/%s/examples" % (get.docDIR(), get.srcNAME())

#def setup():
#	if shelltools.isFile("alsaaudio.o"):
#		shelltools.unlink("alsaaudio.o")

def build():
	pythonmodules.compile(pyVer = "3")

def install():
	pythonmodules.install(pyVer = "3")

#	pisitools.dodoc("LICENSE", "CHANGES", "README.md")
#	pisitools.dohtml("doc/*")
#	pisitools.insinto(examples, "*test.py")

