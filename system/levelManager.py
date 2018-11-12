#
#  /$$   /$$                 /$$           /$$       /$$  /$$$$$$          
# | $$$ | $$                | $$          | $$      |__/ /$$__  $$         
# | $$$$| $$  /$$$$$$   /$$$$$$$  /$$$$$$ | $$       /$$| $$  \__//$$$$$$  
# | $$ $$ $$ /$$__  $$ /$$__  $$ /$$__  $$| $$      | $$| $$$$   /$$__  $$ 
# | $$  $$$$| $$  \ $$| $$  | $$| $$$$$$$$| $$      | $$| $$_/  | $$$$$$$$ 
# | $$\  $$$| $$  | $$| $$  | $$| $$_____/| $$      | $$| $$    | $$_____/ 
# | $$ \  $$|  $$$$$$/|  $$$$$$$|  $$$$$$$| $$$$$$$$| $$| $$    |  $$$$$$$ 
# |__/  \__/ \______/  \_______/ \_______/|________/|__/|__/     \_______/ 
#
# @author Jackthehack21 <gangnam253@gmail.com | Jackthehaxk21#8860>
#
# A small text based game helping a person in distress out in space...
# Copyright (C) 2018 Jackthehack21

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  
# If not, see https://www.gnu.org/licenses/

import os, sys, time, importlib

class manager:
    def __init__(self, game):
        self.game = game
        self.ver = 100 #Must Match Level MetaData (plugins in future 0.2

        self._prefix = 'system.levels.'
        self._levels = {
            '0': 'Introduction',
            '1': 'Hello',
            '2': 'Exploring'
        }

    def getLevel(self, path):
        try:
            return importlib.import_module(path)
        except ImportError:
            self.game.logger.log('[Level Manager] Failed to import path: '+path,3)
        return None

    def getLevelByCode(self, code):
        if(len(self._levels) <= int(code)):
            return self.getLevel(self._prefix+self._levels[code])
        else:
            return None

    def getLevelByName(self, Name):
        for i in range(len(self._levels)):
            if(self._levels[i].lower() == Name.lower()):
                return self.getLevel(self._prefix+self._levels[i])
        return None