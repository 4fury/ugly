#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file http://www.gnu.org/licenses/gpl.txt

#from pisi.actionsapi import shelltools
from pisi.actionsapi import mesontools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

j = "-Dface-detection-helper=false \
     -Dinstall-apport-hook=false \
     -Dface-detection=false \
     -Dextra-plugins=false \
     -Dunity-support=false \
     -Dpublishers='' \
    "

def setup():
	# disable webkit requirement
#	shelltools.system("sed -i '6d;19,20d' plugins/meson.build")
#	shelltools.system("sed -i 's/webkit, //' plugins/meson.build")
#	shelltools.system("sed -i 's/webkit, //' plugins/shotwell-publishing/meson.build")
#	shelltools.system("sed -i 's/gdata, //' plugins/shotwell-publishing/meson.build")
#	shelltools.system("sed -i 's/webkit, //' plugins/shotwell-transitions/meson.build")
#	shelltools.system("sed -i 's/, webkit//' plugins/authenticator/shotwell/meson.build")
#	shelltools.system("sed -i '44d;98d' meson.build")
	mesontools.configure(j)

def build():
	mesontools.build()

def install():
	mesontools.install()

	pisitools.dodoc("AUTHORS", "COPYING", "NEWS", "README.md", "THANKS")

