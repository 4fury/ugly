#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# Licensed under the GNU General Public License, version 3.
# See the file https://www.gnu.org/licenses/gpl-3.0.txt

from pisi.actionsapi import shelltools
from pisi.actionsapi import autotools
from pisi.actionsapi import pisitools
from pisi.actionsapi import get

def setup():
    shelltools.echo("src/feature.h", "#define SYS_VIMRC_FILE \"/etc/vim/vimrc\"")

    # our binary ctags file is names as exuberant-ctags
    pisitools.dosed("runtime/doc/syntax.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/doc/tagsrch.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/doc/usr_29.txt", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")
    pisitools.dosed("runtime/menu.vim", "(ctags(\"| [-*.]|\\s+/))", "exuberant-\\1")

    options ="--with-features=huge \
              --enable-multibyte \
              --enable-perlinterp \
              --enable-pythoninterp \
              --enable-rubyinterp \
              --enable-gui=no \
              --with-tlib=ncurses \
              --prefix=/usr \
              --localstatedir=/var/lib/vim \
              --with-features=big \
              --disable-acl \
              --with-compiledby=PisiLinux \
              --enable-gpm \
              --enable-acl \
              --enable-cscope \
              --disable-netbeans \
              --disable-luainterp \
              --with-x=no \
              --with-modified-by=PisiLinux"

    if get.buildTYPE() == "gui":
        options += " --enable-gui=gtk3 \
                     --with-vim-name=gvim \
                     --with-view-name=gview \
                     --with-x=yes"

    autotools.configure(options)

def build():
    autotools.make()

def install():
    autotools.rawInstall("VIMRCLOC=/etc/vim DESTDIR=%s" % get.installDIR())

    if get.buildTYPE() == "gui":
        return

    pisitools.dosym("vim", "/usr/bin/vi")
    pisitools.dosym("/usr/bin/vim", "/bin/ex")

