#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

t = "Xresources"

def build():
	autotools.make("PREFIX=/usr")

def install():
	autotools.install("PREFIX=/usr")
#	pisitools.dobin("st")

	pisitools.dodoc("FAQ", "LICENSE", "README", "TODO")
#	pisitools.doman("doc/st.1")
	pisitools.doinfo("st.info")
	pisitools.insinto("/usr/share/doc/xst", ".%s" t, "%s" t)

