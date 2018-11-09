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

import time, os, importlib, sys

prefix = 'system.levels.'

levels = {
    "0": "Introduction",
    "1": "Hello",
    "2": "Exploring"
}

def run(game):
    time.sleep(1)
    game.logger.log('Game Details:',0)
    game.logger.log('v'+game.build.ver(),0)
    game.logger.log('build-'+game.build.build(),0)
    sys.stdout.write('---Game info---\n')
    sys.stdout.write('Version - v'+game.build.ver()+'\n')
    sys.stdout.write('Build   - '+game.build.build()+'\n')
    sys.stdout.write('---------------\n')
    time.sleep(2)
    if(game.travis):
        game.logger.log('Skipped save check.',0)
        game.logger.log('Travis Mode Enabled',2)
        level = importlib.import_module(prefix+levels['0'])
        level.exec(game)
        return
    game.logger.log('Checking for saves',0)
    print('\x1b[2J')
    userData = game.userdata.get()
    if(userData):
        game.logger.log('Save found !',0)
        if(str(userData['level']) in levels):
            level = importlib.import_module(prefix+levels[str(userData['level'])])
            level.exec(game)

        else:
            game.logger.log('More levels coming soon !',1)
            input('press enter to exit.')
            return
    else:
        game.logger.log('No saves found.', 0)
        game.logger.log('Loading Intro...', 0)
        level = importlib.import_module(prefix+levels['0'])
        level.exec(game)

    while(True):
        userData = game.userdata.get()
        if(str(userData['level']) in levels):
            print('\x1b[2J')
            level = importlib.import_module(prefix+levels[str(userData['level'])])
            level.exec(game)
            #go back to where he came from, using levels var
        else:
            game.logger.log('More levels coming soon !',1)
            input('press enter to exit.')
            return
