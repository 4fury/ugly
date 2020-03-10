# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
	shelltools.system("NOCONFIGURE=1 ./autogen.sh")
#	autotools.configure("-h")
	autotools.configure("\
	--enable-backup \
	--enable-printing \
	\
	--with-notes \
	--with-tasks \
	\
	--without-contacts")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS", "ChangeLog", "COPYING", "FAQ", "README", "TRANSLATORS")

