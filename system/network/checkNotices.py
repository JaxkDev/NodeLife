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

import json
import time

from system.network import http


def check(game):
    if not http.valid_connection():
        game.logger.log('Failed to retrieve notices, Please check you have a internet connection and is working !', 2)
        return
    r = http.get(game.config.get().get('Network', 'notice_url')+'?app='+game.build.http(), game)
    if not r:
        return
    if r.status != 200:
        game.logger.log('Failed to retrieve notices, error code: '+r.status+'Please create a issue on our github '
                        '<https://github.com/Jackthehack21/NodeLife/issues>', 2)
        return
    game.logger.log('Successfully Got Latest Notices !', 0)
    new = json.loads(r.read().decode("utf-8"))
    f = open('./data/notices.dat', 'a')
    f.close()
    f = open('./data/notices.dat', 'r')
    old = f.read()
    f.close()
    if old == '':
        old = {
            "latest": "0000"
        }
        f = open('./data/notices.dat', 'w')
        f.write(json.dumps(old))
        f.close()
    else:
        old = json.loads(old)
    if old['latest'] == new['latest']:
        game.logger.log('No new notices.', 0)
        return
    else:
        while int(old['latest']) < int(new['latest']):
            old['latest'] = int(old['latest'])+1
            print('')
            print('Notice '+str(old['latest'])+': '+str(new[str(old['latest'])]))
            print('')
        time.sleep(3)
    f = open('./data/notices.dat', 'w')
    f.write(json.dumps(new))
    f.close()
    if not game.travis:
        input('Press enter to continue...')
    return
