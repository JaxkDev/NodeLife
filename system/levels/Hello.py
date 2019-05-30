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

# CHAPTER 1 - HELLO ?
# THE USER WILL LEARN WHAT IS HAPPENING AND GET TO KNOW THE UI.

# pylint: disable=W0612
# Stupid rule

import random
import sys
import time


def save(userdata, levelpart, game):
    userdata['lastPlayed'] = int(round(time.time()))
    userdata['levelPart'] = levelpart
    game.logger.log('Init save...', 0)
    if not game.travis:
        game.threadManager.add(game.userdata.set, (userdata, game,))


def d(userdata, game):
    save(userdata, "d", game)
    time.sleep(0.5)
    game.logger.log('Whats the \'Crystal\' ?\n', 8)
    time.sleep(0.5)
    game.logger.log('Oh right, sorry the \'Crystal\' is a space center, made to travel through space to planets and '
                    'research them, we already gathered data from 3 of the 5 we were sent here to do but something '
                    'happened in the lab...\n', 5)


def c(userdata, game):
    save(userdata, "c", game)
    time.sleep(0.5)
    game.logger.log('What Happened ?\n', 8)
    time.sleep(0.5)
    game.logger.log('Something happened in the lab and half of the Crystal is gone !\n', 5)


def b(userdata, game):
    save(userdata, "b", game)
    other = game.config.get().get('General', 'otherName')
    time.sleep(0.5)
    game.logger.log('Ah yes of course sorry where\'s my manners, My name is \"'+other+'\"\n', 5)
    time.sleep(0.5)
    game.logger.log('Im currently floating around on the Crystal, lost contact with humans about a week ago and '
                    'almost gone through all of my rations...\n', 5)
    time.sleep(0.5)
    while True:
        game.logger.log('\nOption A:  What Happened?\nOption B:  Whats the crystal?\nOption C:  Floating?\n', 6)
        if game.travis:
            response = random.choice(['a', 'b', 'c'])
            break
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if i == 'a' or i == 'b' or i == 'c':
            response = i
            break
    if response == 'a':
        c(userdata, game)
        # Whats the crystal ?
        d(userdata, game)
    elif response == 'b':
        d(userdata, game)
        # what happened ?
        c(userdata, game)
    else:
        game.logger.log('\'Floating\' ?\n', 8)
        time.sleep(0.5)
        game.logger.log('Oops forgot to mention im in outer space in the crystal...\n', 5)
        # whats the crystal ?, what happened ?
        while True:
            game.logger.log('\nOption A:  Whats the crystal ?\nOption B:  What happened?\n', 6)
            if game.travis:
                response = random.choice(['a', 'b'])
                break
            i = input('Type a option: ').lower()
            sys.stdout.write('\n')
            if i == 'a' or i == 'b':
                response = i
                break
        if response == 'a':
            d(userdata, game)
        else:
            c(userdata, game)
            

def a(userdata, game):
    save(userdata, "a", game)
    game.logger.log('Chapter 1 - Hello ?', 1)
    time.sleep(2)
    sys.stdout.write('\033[35m')
    for i in 'INCOMING TRANSMISSION':
        sys.stdout.write(i)
        time.sleep(0.05)
    for i in range(6):
        sys.stdout.write('.')
        time.sleep(0.6)
    sys.stdout.write('.\n\n')
    time.sleep(1)
    sys.stdout.write('CONNECTION ESTABLISHED.\033[39m\n\n\n')
    time.sleep(1.5)
    game.logger.log('[??] : Ugh, Is this damn thing even on...\n', 5)
    while True:
        game.logger.log('\nOption A:  Hello ?\nOption B:  Hi there !\n', 6)
        if game.travis:
            response = random.choice(['a', 'b'])
            break
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if i == 'a' or i == 'b':
            response = i
            break
    if response == 'a':
        game.logger.log('Hello ?\n', 8)
        time.sleep(0.5)
        game.logger.log('[??] : Hello !!????\nWas that someone ???\n', 5)
        time.sleep(0.5)
        game.logger.log('Yes, Hello ?\n', 8)
    else:
        game.logger.log('Hi there !\n', 8)
        time.sleep(0.5)
        game.logger.log('[??] : Yes, Yes i knew i wasn\'t alone i knew someone would rescue me !\n', 5)
        time.sleep(0.5)
        game.logger.log('[??] : Of course they sent someone, why wouldn\'t they !\n', 5)
        time.sleep(0.5)
        game.logger.log('Erm, Hello ?\n', 8)
    b(userdata, game)


def exec(game):
    userdata = game.userdata.get()
    if not userdata:
        game.logger.log('Corrupt Data...', 3)
        input('Press enter to exit.')
        sys.exit(1)

    game.logger.log('Loading Stage...', 0)
    if userdata['levelPart'] == 'a' or userdata['levelPart'] == '-':
        a(userdata, game)
    elif userdata['levelPart'] == 'b':
        b(userdata, game)
    elif userdata['levelPart'] == 'c':
        c(userdata, game)
    elif userdata['levelPart'] == 'd':
        d(userdata, game)
    time.sleep(0.5)
    game.logger.log('Cleared chapter 1, Cleared User Display', 0)
    game.logger.log('Saving Data, do not exit the game', 2)
    userdata['lastPlayed'] = int(round(time.time()))
    userdata['level'] = 2
    userdata['levelPart'] = '-'
    game.logger.log('Init save thread...', 0)
    if not game.travis:
        game.threadManager.add(game.userdata.set, (userdata, game,))
    if not game.travis:
        game.logger.log('Save complete, would you like to end the game for today or move onto chapter 2 ?', 1)
        i = input('Quit ? (yes/no) > ').lower()
        if i[0] == 'y':
            sys.exit(0)  # status code 0- normal.
        time.sleep(1)
        input('Press enter to continue..')
    print('\x1b[2J')
    game.logger.log('Chapter 1 ended', 0)
    game.levelManager.runlevel('2')
