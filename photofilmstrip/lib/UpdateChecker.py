# -*- coding: utf-8 -*-
#
# PhotoFilmStrip - Creates movies out of your pictures.
#
# Copyright (C) 2008 Jens Goepfert
#

import threading
#import urllib.request
#import re

from photofilmstrip import Constants


class UpdateChecker(threading.Thread):

    URL = Constants.APP_URL + "/update.txt"

    def __init__(self):
        threading.Thread.__init__(self, name="UpdateCheck")

        self._onlineVersion = None
        self._changes = []
        self._checkDone = False
        self._isOk = False

        self.start()

    def run(self):
        """
        We deactivate the Update Check here for the time being
        """
        #try:
        #    fd = urllib.request.urlopen(self.URL)
        #    #fd = open('/home/jens/Projects/Python/PhotoFilmStrip/res/update.txt', 'r')
        #    data = fd.read()
        #except IOError:
        #    self._checkDone = True
        #    return

        #lines = data.decode("utf-8").split('\n')

        #ovMatch = re.match(r"(\d+).(\d+).(\d+)?(.+)?", lines.pop(0))
        #if ovMatch:
        #    self._onlineVersion = ".".join(ovMatch.groups()[:3])
        #else:
        #    return

        #self._changes = lines

        self._checkDone = True
        self._isOk = True

    def IsDone(self):
        return self._checkDone

    def IsOk(self):
        return self._isOk

    def IsNewer(self, currentVersion):
        """
        We deactivate the Update Check here for the time being
        """
        #if self.IsDone() and self.IsOk():
        #    #curTup = currentVersion.split(".")
        #    #newTup = self._onlineVersion.split(".")
        #    return newTup > curTup
        return False

    def GetChanges(self):
        return "\n".join(self._changes)

    def GetVersion(self):
        return self._onlineVersion
