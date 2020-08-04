#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "--with-gl \
     --with-gtk \
     --with-xft \
     --with-pam \
     --with-shadow \
     --with-dpms-ext \
     --with-xshm-ext \
     --with-xdbe-ext \
     --without-systemd \
    "

def setup():
	autotools.configure(j)

def build():
	autotools.make()

def install():
	autotools.rawInstall("nstall_prefix=%s" % get.installDIR())

	pisitools.dodoc("INSTALL", "README", "README.hacking", "README.VMS")

