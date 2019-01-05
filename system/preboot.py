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

import ssl, os, time, sys
from system import setup
from system.resources import list
from system.network import getResources, http

def run(game):
    # This is to fis SSL error when checking for update on MacOSX.
    eval(game.os.system.lower()+'()')
    resources(game)
    setup.exec(game)
    return

def windows():
    return

def linux():
    return

def darwin():
    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        # Legacy Python that doesn't verify HTTPS certificates by default
        pass
    else:
        # Handle target environment that doesn't support HTTPS verification
        ssl._create_default_https_context = _create_unverified_https_context
    return

def resources(game):


    #use resources list here. ( list.get() )



    try:
        f = open('data/resources/config.txt','r')
        f.close()
    except Exception:
        try:
            os.makedirs('data/resources')
        except Exception:
            game.logger.log('Resource folder found, but no data.',0) #aborted download.
        if(not http.valid_connection()):
            game.logger.log('A valid internet connection is required for first time boot.',3)
            sys.exit(0)
        data = getResources.info(game,'config.txt').read().decode('utf-8')
        size = data.split('#')[1]
        data = data.split('#')[0]
        if(game.travis):
            choice = 'yes'
        else:
            choice = input('The game needs to download the file \'Config.txt\' size: '+size+', Download now ? (yes/no): ').lower() 
        if(choice != 'yes'):
            game.logger.log('Game resources download aborted.',2)
            time.sleep(2)
            sys.exit(0)
        url = data.split('/')
        file = url[-1]
        del url[-1]
        url = '/'.join(url)
        game.logger.log('Getting resource at '+url+'/'+file,0)
        getResources.get(game,file,url)

    try:
        f = open('data/resources/MainLoop.mp3','r')
        f.close()
    except Exception:
        try:
            os.makedirs('data/resources')
        except Exception:
            game.logger.log('Resource folder found, but no data, possibly aborted download.',0) #aborted download.
        data = getResources.info(game,'loopsound.txt').read().decode('utf-8')
        size = data.split('#')[1]
        data = data.split('#')[0]
        if(game.travis):
            choice = 'yes'
        else:
            choice = input('The game needs to download the file \'LoopSound.mp3\' size: '+size+', Download now ? (yes/no): ').lower() 
        if(choice != 'yes'):
            game.logger.log('Game resources download aborted.',2)
            time.sleep(2)
            sys.exit(0)
        url = data.split('/')
        file = url[-1]
        del url[-1]
        url = '/'.join(url)
        game.logger.log('Getting resource at '+url+'/'+file,0)
        game.logger.log('Getting resource meta file as well.',0)
        getResources.get(game,file,url,'MainLoop.mp3')
        getResources.get(game,"MainLoop.meta",customName='MainLoop.meta')
    return