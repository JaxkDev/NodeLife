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

from system.utils import logger
from system.network import http
from system import ver
from urllib import request, error
import json

def check(travis):
    if(not http.valid_connection()):
        logger.log('Failed to retrieve update information, Please check your internet connection !',2)
        return
    r = http.get('https://fusioncraft.glitch.me/NodeLife/update?app='+ver.http())
    if(r == False):
        return
    if(r.status != 200):
        logger.log('Failed to retrieve update information, error code: '+r.status+' Please create a issue on our github <https://github.com/Jackthehack21/NodeLife/issues>', 2)
        return
    logger.log('Successfully Got Update Information', 0)
    data = json.loads(r.read().decode("utf-8"))
    logger.log('Received Data from server: '+str(data), 0)
    if(canUpdate(ver.ver(), data['ver'])):
        logger.log('Update '+data['ver']+' is available at '+data['url'], 2)
        if(not travis):
            #Show UI here
            input('\nPress any key to continue...\n')
    else:
        logger.log('Game Up-To-Date !', 0)
    
    return

def canUpdate(n, n2):
    original = n.split('.')
    available = n2.split('.')
    if(int(original[0]) < int(available[0])):
        return True
    if(int(original[1]) < int(available[1])):
        return True
    if(int(original[2]) < int(available[2])):
        return True
    return False