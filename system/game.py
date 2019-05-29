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

import platform

from system import levelManager as lvlMgr
from system import threadingManager as thrdMgr
from system import ver
from system.utils import logger, config, userdata


#
# Right lets sort this out.
# Instead of passing around a load of functions vars, etc
# Were going to create a base ‘game’ class
# it will hold all major factors eg
# - Travis ?
# - Logger
# - UserData
# - threading manager (coming soon)
# - level manager (coming soon)


class Game:

    # Initializer / Instance Attributes
    def __init__(self, travis):
        self.travis = travis
        self.logger = logger.Logger(self)
        self.config = config
        self.userdata = userdata
        self.build = ver
        self.os = platform.uname()
        self.levelManager = lvlMgr.Manager(self)
        # self.resourceManager (overwrite current preboot)
        self.threadManager = thrdMgr.Manager(self)
        # to stop threads being used up for now:
        # self.soundManager = snd.manager(self)
        # SFS (Simple File System) (after 1.0)
