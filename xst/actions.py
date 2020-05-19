#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools

def build():
	autotools.make("PREFIX=/usr")

def install():
	pisitools.dobin("st")

	pisitools.dodoc("README.md", "doc/LICENSE", "doc/Xresources")
	pisitools.doman("doc/st.1")
	pisitools.doinfo("doc/st.info")

