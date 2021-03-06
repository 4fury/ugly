#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--enable-cplusplus \
     --enaible-curl-client \
     --disable-cgi-server \
     --disable-libwww-client \
     --disable-wininet-client \
     --disable-libxml2-backend \
    "

def setup():
	autotools.configure(j)

def build():
	autotools.make()

#def check():
#	autotools.make("check")

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("README")

