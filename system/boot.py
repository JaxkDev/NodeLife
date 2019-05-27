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

import time, sys, datetime

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
        game.levelManager.runLevel('0')
        return
    game.logger.log('Checking for saves',0)
    print('\x1b[2J')
    userData = game.userdata.get()
    if(userData):
        game.logger.log('Save found !',0)
        #Check for time delay (Sleeping, walking etc)
        if 'timeCheck' in userData:
            game.logger.log("Found TimeCheck active: "+str(userData['timeCheck']),0)
            if(userData['timeCheck'] > time.time()):
                #Still away.
                cfg = game.config.get()
                other_name = cfg.get('General','otherName')
                del cfg #no conflicts.
                tmp = datetime.timedelta(seconds=userData['timeCheck']-int(time.time()))
                #datetime.timedelta(0, 65)
                timeLeft = str(tmp)
                del tmp #no conflicts
                game.logger.log(other_name+" is still away, please come back in "+timeLeft+" (HH:MM:SS)",1)
                input('Press enter to exit !')
                return
            else:
                del userData['timeCheck']
                game.logger.log("Deleted timeCheck, time is valid.",0)
        if(int(userData['level']) < len(game.levelManager.levels)):
            game.levelManager.runLevel(str(userData['level']))
    else:
        game.logger.log('No saves found.', 0)
        game.levelManager.runLevel('0')
    game.logger.log('More chapters coming soon !',1)
    input('Press enter to exit !')
    return