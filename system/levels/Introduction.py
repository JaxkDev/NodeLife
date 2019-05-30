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

# CHAPTER 0 - Introduction
# THE USER WILL LEARN WHAT THIS GAME IS.

# pylint: disable=W0612
# Stupid rule

import platform
import sys
import time

speeds = {
    "veryslow": 0.2,
    "slow": 0.14,
    "normal": 0.09,
    "fast": 0.05,
    "insane": 0.01
}


def slow(txt, game):
    if platform.uname().system.lower() != "windows":
        sys.stdout.write(txt)
        return
    if game.config.get().get("Graphics", "slow_text").lower() == "yes":
        for i in txt:
            sys.stdout.write(i)
            time.sleep(speeds[game.config.get().get("Graphics", "slow_text_speed").lower()])
    else:
        sys.stdout.write(txt)


def a(game):
    slow('Hi there !', game)
    sys.stdout.write('\n\n')
    time.sleep(0.5)
    slow('This game was made possible by me Jack Honour (aka Jackthehack)', game)
    sys.stdout.write('\n')
    slow('this was originally made for educational purposes but was soon developed further and is now a on going '
         'project, Originally started in JavaScript it is now all in pure python', game)
    sys.stdout.write('\n')
    slow('it is fully open-source (github.com/Jackthehack21/NodeLife) and does accept PR\'s and feature requests', game)
    sys.stdout.write('\n')
    slow('If you want to see something in the game create a issue and choose feature request template, or if your not '
         'on github im on Discord ! (Jackthehaxk21#8860)', game)
    sys.stdout.write('\n\n\033[32mAbout the Game:\033[39m\n')
    slow('You are a communication expert working in NASA\'s HQ, one day while eating doughnuts you receive a '
         'transmission from coordinates not located on earth, but somewhere out there in space.', game)
    sys.stdout.write('\n')
    slow('you begin talking to this person on the other end and guide them to safety, '
         'can you help him survive !?...', game)
    sys.stdout.write('\n\n')
    time.sleep(10)
    if not game.travis:
        input('Press enter to start the game !')


def exec(game):
    userdata = game.userdata.get()
    if userdata != {}:
        game.logger.log('Corrupt Data found, please delete the data/user folder.', 3)
        if not game.travis:
            input('Press enter to continue...')
        sys.exit(1)
    a(game)
    game.logger.log('Saving game...\n', 1)
    userdata['lastPlayed'] = int(round(time.time()))
    userdata['level'] = 1
    userdata['levelPart'] = '-'
    game.logger.log('Init save...', 0)
    game.threadManager.add(game.userdata.set, (userdata, game,))
    time.sleep(2)
    print('\x1b[2J')
    game.levelManager.runlevel('1')
