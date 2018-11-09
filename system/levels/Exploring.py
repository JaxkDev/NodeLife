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

# CHAPTER 2 - What was that ? / Exploring
# THE USER WILL HELP MIKE, CHOOSE ESSENTIALS AND EXPLORE THE CRYSTAL.

#pylint: disable=W0612
#Stupid rule

import sys, time, random, os, _thread, platform

def slow(txt, delay):
    if(platform.uname().system.lower() != "windows"):
        sys.stdout.write(txt)
        return
    for i in txt:
        sys.stdout.write(i)
        time.sleep(delay)


def save(userData, levelPart, game):
    userData['lastPlayed'] = int(round(time.time() * 1000))
    userData['levelPart'] = levelPart
    game.logger.log('Init save thread...',0)
    _thread.start_new_thread( game.userdata.set, (userData, game,) ) # multi-thread


def c(user, game):
    save(user,"c",game)
    game.logger.log("c",0)

def b(user, game):
    save(user,"b",game)
    game.logger.log("b",0)

def a(user, game):
    save(user,"a",game)
    game.logger.log("a",0)

def exec(game):
    userData = game.userdata.get()
    if(userData == {}):
        game.logger.log('Corrupt Data found, please delete the data/user folder.',3)
        input('Press enter to exit.')
        sys.exit(1)
    a(userData, game)
    game.logger.log('Saving game...',1)
    userData['lastPlayed'] = int(round(time.time() * 1000))
    userData['level'] = 3
    userData['levelPart'] = '-'
    game.logger.log('Init save function...',0)
    game.userdata.set(userData, game)
