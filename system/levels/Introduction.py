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

# CHAPTER 0 - Introduction
# THE USER WILL LEARN WHAT THIS GAME IS.

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

def a(user, game):
    slow('Hi there !', 0.05)
    sys.stdout.write('\n\n')
    time.sleep(0.5)
    slow('This game was made possible by me Jack Honour (aka Jackthehack)', 0.1)
    sys.stdout.write('\n')
    slow('this was originally made for educational purposes but was soon developed further and is now a on going project, Originally started in JavaScript it is now all in pure python', 0.1)
    sys.stdout.write('\n')
    slow('it is fully open-source (github.com/Jackthehack21/NodeLife) and does accept PR\'s and feature requests',0.1)
    sys.stdout.write('\n')
    slow('If you want to see something in the game create a issue and choose feature request template, or if your not on github im on Discord ! (Jackthehaxk21#8860)',0.1)
    sys.stdout.write('\n')
    sys.stdout.write('\n\n\n\033[32mAbout the Game:\033[39m\n')
    slow('You are a communication expert working in NASA\'s HQ, one day while eating doughnuts you recieve a transmission from coordinates not located on earth, but somewhere out there in space.',0.1)
    sys.stdout.write('\n')
    slow('you begin talking to this person on the other end and guide them to safety, can you help him survive !?...',0.1)
    sys.stdout.write('\n\n')
    time.sleep(10)
    if(not game.travis):
        input('Press enter to start the game !')

def exec(game):
    userData = game.userdata.get()
    if(userData != {}):
        game.logger.log('Corrupt Data found, please delete the data/user folder.',3)
        if(not game.travis):
            input('Press enter to continue...')
        sys.exit(1)
    a(userData, game)
    game.logger.log('Saving game...',1)
    userData['lastPlayed'] = int(round(time.time() * 1000))
    userData['level'] = 1
    userData['levelPart'] = '-'
    game.logger.log('Init save thread...',0)
    game.userdata.set(userData, game)
    print('')
    time.sleep(2)
    game.levelManager.runLevel('1')
