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

import os, sys, json, getpass
import system.utils.secure as sec

def getLoginName():
	return os.environ['SUDO_USER'] if 'SUDO_USER' in os.environ else getpass.getuser()

def get():
    #Get user data
    if(not os.path.exists('data/')):
        os.mkdir('data')
        return {}
    if(not os.path.exists('data/user/')):
        os.mkdir('data/user')
        return {}
    if(not os.path.isfile('data/user/data.secure')):
        return {}
    
    f = open('data/user/data.secure', 'r')

    #print("")
    #print(sec.getKey())
    #print("")
    #decode data (f.read())
    data = json.loads(f.read()) #do json after decode when implemented
    f.close()
    return data

def set(data, game):
    #Set user data
    game.logger.log('Started save user data thread',0)
    if(not os.path.exists('data/')):
        os.mkdir('data')
    if(not os.path.exists('data/user/')):
        os.mkdir('data/user')
    #encode data
    f = open('data/user/data.secure', 'w')
    f.write(json.dumps(data)) #do json before encode when implemented
    f.close()
    #TODO: Add X backups (X in config)
    game.logger.log('Completed save user data thread',0)
    return