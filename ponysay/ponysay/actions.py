#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import pythonmodules
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

## bug: text output with double underline

i = "--freedom=partial \
     --everything \
     --with-bash \
     --without-info \
     --dest-dir=%s \
    " % get.installDIR()

def install():
	shelltools.system("python3 setup.py install %s" % i)
	pisitools.removeDir("var")

	pisitools.dodoc("CHANGELOG", "CONTRIBUTING", "README.md")

