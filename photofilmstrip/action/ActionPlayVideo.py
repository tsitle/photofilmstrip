# -*- coding: utf-8 -*-
#
# PhotoFilmStrip - Creates movies out of your pictures.
#
# Copyright (C) 2011 Jens Goepfert
#

import os
#from gettext import gettext as _  # only to point out where the function '_()' comes from - but do not actually import - it won't work

from photofilmstrip.action.IAction import IAction
from photofilmstrip.lib.util import StartFile


class ActionPlayVideo(IAction):

    def __init__(self, outFile):
        self.outFile = outFile

    def GetName(self):
        return _("Play video")

    def Execute(self):
        if os.path.isfile(self.outFile):
            StartFile(self.outFile)
