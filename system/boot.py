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

from system.utils import logger, userdata
import time, os, importlib, system.ver, sys

def pr(msg, lvl):
    logger.log(msg, lvl)

prefix = 'system.levels.'

levels = {
    "0": "Introduction",
    "1": "Hello"
}

def run(Travis):
    time.sleep(1)
    pr('Game Details:',0)
    pr('v'+system.ver.ver(),0)
    pr('build-'+system.ver.build(),0)
    sys.stdout.write('---Game info---\n')
    sys.stdout.write('Version - v'+system.ver.ver()+'\n')
    sys.stdout.write('Build   - '+system.ver.build()+'\n')
    sys.stdout.write('---------------\n')
    time.sleep(2)
    print('\x1b[2J')
    if(Travis):
        pr('Skipped save check.',0)
        pr('Travis Mode Enabled',2)
        level = importlib.import_module(prefix+levels['0'])
        level.exec({}, pr, True)
        return
    pr('Checking for saves',0)
    userData = userdata.get()
    if(userData):
        level = importlib.import_module(prefix+levels[str(userData['level'])])
        level.exec(userData, pr, False)
        #go back to where he came from, using levels var
    else:
        pr('No saves found.', 0)
        pr('Loading Intro...', 0)
        level = importlib.import_module(prefix+levels['0'])
        level.exec(userData, pr, False)

    while(True):
        userData = userdata.get()
        if(len(levels)-1 > userData['level']):
            pr('More coming soon !',1)
            input('Press enter to exit.')
            sys.exit(0)
        print('\x1b[2J')
        level = importlib.import_module(prefix+levels[str(userData['level'])])
        level.exec(userData, pr, False)
    #go to next chapter.
