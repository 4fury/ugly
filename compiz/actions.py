#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import cmaketools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

p = "%s" % get.curPYTHON()

def setup():
	shelltools.system("sed -i '18,23s/^/#/' cmake/recompile_gsettings_schemas_in_dir_user_env.cmake")
	shelltools.makedirs("build")
	shelltools.cd("build")
	cmaketools.configure("\
	\
	-DCMAKE_BUILD_TYPE=Release \
	-DCMAKE_INSTALL_LIBDIR=lib \
	\
	-DCOMPIZ_DEFAULT_PLUGINS=\
	addhelper \
	animation \
	animationaddon \
	animationjc \
	animationplus \
	annotate \
	blur \
	ccp \
	clone \
	colorfilter \
	commands \
	compiztoolbox \
	composite \
	copytex \
	crashhandler \
	cube \
	cubeaddon \
	dbus \
	decor \
	expo \
	extrawm \
	ezoom \
	fade \
	fadedesktop \
	firepaint \
	gnomecompat \
	grid \
	imgjpeg \
	imgpng \
	imgsvg \
	inotify \
	mag \
	matecompat \
	maximumize \
	mousepoll \
	move \
	neg \
	notification \
	obs \
	opacify \
	opengl \
	place \
	put \
	regex \
	resize \
	resizeinfo \
	ring \
	rotate \
	scale \
	scaleaddon \
	scalefilter \
	screenshot \
	session \
	shelf \
	shift \
	showdesktop \
	showmouse \
	showrepaint \
	simple-animations \
	snap \
	splash \
	staticswitcher \
	switcher \
	text \
	titleinfo \
	trailfocus \
	vpswitch \
	wall \
	wallpaper \
	water \
	winrules \
	wizard \
	wobbly \
	workarounds \
	workspacenames \
	\
	-DBUILD_GTK=ON \
	-DBUILD_GLES=ON \
	-DBUILD_GNOME=ON \
	-DBUILD_METACITY=ON \
	-DCYTHON_BIN=/usr/bin/cython \
	-DPYTHON_EXECUTABLE=/usr/bin/python3 \
	-DPYTHON_LIBRARY=/usr/lib/libpython%sm.so \
	-DPYTHON_INCLUDE_DIR=/usr/include/python%sm -L" % (p, p), sourceDir = '..')

def build():
	shelltools.cd("build")
	cmaketools.make()

def install():
	shelltools.cd("build")
	cmaketools.rawInstall("DESTDIR=%s" % get.installDIR())

	shelltools.cd("..")
	pisitools.dodoc("AUTHORS", "COPYING*", "NEWS", "README")

