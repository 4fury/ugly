#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import perlmodules
from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

KeepSpecial=["libtool"]

j = "--program-transform-name=imagemagick6 \
     --docdir=/usr/share/doc/imagemagick6 \
     --enable-hdri \
     --enable-shared \
     --disable-static \
     --with-x \
     --with-wmf \
     --with-xml \
     --with-jp2 \
     --with-zlib \
     --with-tiff \
     --with-perl \
     --with-rsvg \
     --with-jpeg \
     --with-djvi \
     --with-bzlib \
     --with-gslib \
     --with-lcms2 \
     --with-modules \
     --with-threads \
     --with-magick_plus_plus \
     --with-perl-options='INSTALLDIRS=vendor' \
     --with-gs-font-dir=/usr/share/fonts/defaul/ghostscript \
     --without-fpx \
     --without-dps \
     --without-jbig \
    "

def setup():
	pisitools.dosed("configure.ac", "AC_PATH_XTRA")
	autotools.autoreconf("-fi")

	pisitools.dosed("configure", "DOCUMENTATION_RELATIVE_PATH=.*", "DOCUMENTATION_RELATIVE_PATH=%s/html" % get.srcNAME())
	autotools.configure(j)
	pisitools.dosed("libtool", " -shared ", " -Wl,-O1,--as-needed -shared ")

def build():
	autotools.make()

def install():
	autotools.rawInstall("DESTDIR=%s" % get.installDIR())

	pisitools.dodoc("AUTHORS.txt", "ChangeLog", "LICENSE", "NEWS.txt")

	pisitools.remove("/usr/lib/*.la")

	perlmodules.removePacklist()
	perlmodules.removePodfiles()

