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
import datetime
import platform
import time

from system.network import http


def exec(data, game):
    try:
        if not game.config.get().getboolean('Network', 'upload_error'):
            game.logger.log('PostError disabled', 1)
            return
    except FileNotFoundError:
        return
    game.logger.log('postError Started !', 0)
    time.sleep(1)  # Allow logger to close file
    date = datetime.datetime.now().strftime("%d.%m.%Y")
    logfile= open('data/logs/' + date + '.log', 'r')
    log = logfile.read()
    logfile.close()
    postdata = {
        "log": log,
        "msg": data[0],
        "contact": data[1],
        "ver": game.build.build(),
        "sys": platform.uname()
    }
    if http.valid_connection():
        r = http.post(game.config.get().get('Network', 'upload_error_url'), postdata, game)
    else:
        game.logger.log('No connection unable to post error data', 2)
        return False
        
    return r.status == '200'
