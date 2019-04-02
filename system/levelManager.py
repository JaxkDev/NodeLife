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
# Copyright (C) 2019 Jackthehack21

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
        self.ver = 100 #Must Match Level MetaData (plugins in future 0.2)

        self.prefix = 'system.levels.'
        self.levels = {
            '0': 'Introduction',
            '1': 'Hello',
            '2': 'Exploring'
        }

    def getLevel(self, path):
        try:
            return importlib.import_module(path)
        except ImportError:
            self.game.logger.log('[Level Manager] : Failed to import path: '+path,3)
        return None

    def getLevelByCode(self, code):
        if(len(self.levels) > int(code)):
            return self.getLevel(self.prefix+self.levels[code])
        else:
            return None

    def getLevelByName(self, Name):
        for i in range(len(self.levels)):
            if(self.levels[str(i)].lower() == Name.lower()):
                return self.getLevel(self.prefix+self.levels[i])
        return None

    def runLevel(self, lvl):
        level = self.getLevelByName(lvl)
        if(level == None):
            level = self.getLevelByCode(lvl)
        if(level == None):
            self.game.logger.log('[Level Manager] : Failed to import and run level: '+lvl,3)
            return False
        #Check level metadata with self.ver and self.game.ver
        level.exec(self.game)
        return True