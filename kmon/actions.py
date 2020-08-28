#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import pisitools

def build():
	shelltools.system("cargo build --release --locked --all-features")

def check():
	shelltools.system("cargo test --release --locked")

def install():
	pisitools.dobin("kmon")
	pisitools.doman("kmon.8")

	pisitools.dodoc("CHANGELOG.md", "CONTRIBUTING.md", "LICENSE")

