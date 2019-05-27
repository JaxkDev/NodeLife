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

# This program is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.
# If not, see https://www.gnu.org/licenses/

import time

from system.utils import sound

class manager:
    def __init__(self, game):
        self.game = game
        
        self._list = list()
        
        self._active = list()

        self.game.logger.log('[SoundMgr] : Handler Starting...',0)
        self.game.threadManager.add(self.handler, (), "SoundManager")

    def add(self, soundName, loop=1): #SoundName to be exact in data/resource and loop is default 1
        self._list.append({
            'file': 'data/resources/'+soundName+'.mp3',
            'meta': 'data/resources/'+soundName+'.meta',
            'loop': loop
        })


        #
        # Note:
        #
        # Possibly may have to add amount of seconds/milliseconds it runs for for the loop to work...
        # EDIT: Added .meta files to hold length time.
        
    def handler(self):
        self.game.logger.log('[SoundMgr] : Handler Started.',0)
        while(True):
            time.sleep(0.2) #Todo config
            