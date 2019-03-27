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
#pylint: disable=W0101
#Stupid rule

import sys, time, random, os, platform

def save(userData, levelPart, game):
    userData['lastPlayed'] = int(round(time.time()))
    userData['levelPart'] = levelPart
    game.logger.log('Init save thread...',0)
    if(game.travis == False):
        game.threadManager.add(game.userdata.set, (userData, game,))


def c(userData, game):
    return

def b(userData, game):
    save(userData,"b",game)
    game.logger.log("Im back !",5)
    time.sleep(0.5)
    game.logger.log('You would not believe the dreams i had !',5)
    time.sleep(0.5)
    return

def a(userData, game):
    save(userData,"a",game)
    game.logger.log("Chapter 2 - Exploring",1)
    time.sleep(2)
    sys.stdout.write('\n\033[35mCONNECTION RE-ESTABLISHED.\033[39m\n\n\n')
    time.sleep(0.5)
    game.logger.log('Hello?...Hello anyone there ?\n', 5)
    time.sleep(0.5)
    while(True):
        game.logger.log('\nOption A:  Yeah im here !\nOption B:  Im back, anything new ?\n', 6)
        if(game.travis):
            response = random.choice(['a','b'])
            break
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if(i == 'a' or i == 'b'):
            response = i
            break
    if(response == 'a'):
        game.logger.log('Yeah im here !\n',8)
        time.sleep(1)
        game.logger.log('Oh thank god, I wasnt sure if the communication system survived, thought the whole system was fried !\n',5)
    else:
        game.logger.log('Im back, anything new ?\n',8)
        time.sleep(1)
        game.logger.log('Im glad your back, seriously i thought all the systems were toast !\n',5)
    time.sleep(1)
    while(True):
        game.logger.log('\nOption A:  Wait, Systems were almost gone ?\nOption B:  What happened while i was gone ???\n', 6)
        if(game.travis):
            response = random.choice(['a','b'])
            break
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if(i == 'a' or i == 'b'):
            response = i
            break
    if(response == 'a'):
        game.logger.log('Wait, Systems were almost gone ?\n',8)
        time.sleep(0.5)
        game.logger.log('Yes, the whole system went dark for about 5minutes before the generator kicked in, BUT my power is down to 20% and my generator hasn\'t got alot of juice left...\n',5)
    else:
        game.logger.log('What happened while i was gone ???\n',8)
        time.sleep(0.5)
        game.logger.log('Not alot just lost all power for 5minutes and sat in the freezing cold because i have barely any energy left for the heaters, You would think that they would add better heating incase of these types of emergency\'s but No, they spent as little as possible on this rust bucket.\n',5)
    time.sleep(1)
    game.logger.log('FYI ive been awake for 30hours straight now and need to get some rest, i\'ll see you soon !\n',5)
    #WAIT 12 HOURS
    time.sleep(0.5)
    #12 hours sleep. (60secs*60min*12hours)
    userData['timeCheck'] = int(round(time.time()))+60#(60*(60*12)) #used to check time difference for sleeping.
    save(userData,"b",game)
    time.sleep(2)
    if(not game.travis):
        input("Press enter to exit")
    time.sleep(2)
    sys.exit(0)
    #game.kill(false) args: true/false force close threads.

def exec(game):
    userData = game.userdata.get()
    if(userData == {}):
        game.logger.log('Corrupt Data found, please delete the data/user folder.',3)
        input('Press enter to exit.')
        sys.exit(1)
    game.logger.log('Loading Stage...',0)
    if(userData['levelPart'] == 'a'):
        a(userData, game)
    elif(userData['levelPart'] == 'b'):
        b(userData, game)
    elif(userData['levelPart'] == 'c'):
        c(userData, game)
    game.logger.log('Saving game...',1)
    userData['lastPlayed'] = int(round(time.time()))
    userData['level'] = 3
    userData['levelPart'] = '-'
    game.logger.log('Init save function...',0)
    if(game.travis == False):
        game.threadManager.add(game.userdata.set, (userData, game,))
    #game.levelManager.runLevel('3/4')