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

from system.network import http

def get(game, fileName, url='https://nodelife.glitch.me/api/get/resources', customName=None):
    game.logger.log('Getting resource \''+fileName+'\', please don\'t exit...',2)
    if(customName == None):
        resp = http.download(url+'/'+fileName, 'data/resources/'+fileName, game)
    else:
        resp = http.download(url+'/'+fileName, 'data/resources/'+customName, game)
    if(resp == 0):
        game.logger.log('Success !',1)
    return resp

def info(game, fileName):
    game.logger.log('Getting resource info (HTTP-get)\''+fileName+'\'.',0)
    data = http.get('https://nodelife.glitch.me/api/get/info/'+fileName+'?app='+game.build.http(), game)
    game.logger.log('Success !',0)
    return data
