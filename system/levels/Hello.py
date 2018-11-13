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

# CHAPTER 1 - HELLO ?
# THE USER WILL LEARN WHAT IS HAPPENING AND GET TO KNOW THE UI.

#pylint: disable=W0612
#Stupid rule

import sys, time, random, os, _thread

def save(userData, levelPart, game):
    userData['lastPlayed'] = int(round(time.time() * 1000))
    userData['levelPart'] = levelPart
    game.logger.log('Init save thread...',0)
    _thread.start_new_thread( game.userdata.set, (userData, game,) ) # multi-thread

def d(userData, game):
    save(userData,"d",game)
    user = userData['username']
    time.sleep(0.5)
    game.logger.log(user+' : Whats the \'Crystal\' ?\n',8)
    time.sleep(0.5)
    game.logger.log('[Mike] : Oh right, sorry the \'Crystal\' is a space center, made to travel through space to planets and research them, we already gathered data from 3 of the 5 we were sent here to do but something happened in the lab...\n', 5)

def c(userData, game):
    save(userData, "c",game)
    user = userData['username']
    time.sleep(0.5)
    game.logger.log(user+' : What Happened ?\n', 8)
    time.sleep(0.5)
    game.logger.log('[Mike] : Something happened in the lab and half of the Crystal is gone !\n', 5)
        
def b(userData, game):
    save(userData,"b",game)
    user = userData['username']
    time.sleep(0.5)
    game.logger.log('[Mike] : Ah yes of course sorry where\'s my manners, My name is \"Mike\"\n', 5)
    time.sleep(0.5)
    game.logger.log('[Mike] : Im currently floating around on the Crystal, lost contact with humans about a week ago and almost gone through all of my rations...\n', 5)
    time.sleep(0.5)
    response = ''
    while(True):
        game.logger.log('\nOption A:  What Happened?\nOption B:  Whats the crystal?\nOption C:  Floating?\n', 6)
        if(game.travis):
            response = random.choice(['a','b','c'])
            break
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if(i == 'a' or i == 'b' or i == 'c'):
            response = i
            break
    if(response == 'a'):
        c(userData, game)
        #Whats the crystal ?
        d(userData, game)
    elif(response == 'b'):
        d(userData, game)
        #what happened ?
        c(userData, game)
    else:
        game.logger.log(user+' : \'Floating\' ?\n',8)
        time.sleep(0.5)
        game.logger.log('[Mike] : Oops forgot to mention im in outer space in the crystal...', 5)
        #whats the crystal ?, what happened ?
        while(True):
            game.logger.log('\nOption A:  Whats the crystal ?\nOption B:  What happened?\n', 6)
            if(game.travis):
                response = random.choice(['a','b'])
                break
            i = input('Type a option: ').lower()
            sys.stdout.write('\n')
            if(i == 'a' or i == 'b'):
                response = i
                break
        if(response == 'a'):
            d(userData, game)
        else:
            c(userData, game)
            

def a(userData, game):
    save(userData,"a",game)
    user = userData['username']
    game.logger.log('Chapter 1 - Hello ?',1)
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
    game.logger.log('[??] : Ugh, Maybe one day they\'ll send someone to fetch my body...\n',5)
    response = ''
    while(True):
        game.logger.log('\nOption A:  Hello ?\nOption B:  Hi there !\n', 6)
        if(game.travis):
            response = random.choice(['a','b'])
            break
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if(i == 'a' or i == 'b'):
            response = i
            break
    if(response == 'a'):
        game.logger.log(user+' : Hello ?\n', 8)
        time.sleep(0.5)
        game.logger.log('[??] : Hello !!????\nWas that someone ???\n',5)
        time.sleep(0.5)
        game.logger.log(user+' : Yes, Hello ?\n', 8)
    else:
        game.logger.log(user+' : Hi there !\n',8)
        time.sleep(0.5)
        game.logger.log('[??] : Yes, Yes i knew i wasnt alone i knew someone would rescue me !\n', 5)
        time.sleep(0.5)
        game.logger.log('[??] : Of course they sent someone, why wouldnt they !\n', 5)
        time.sleep(0.5)
        game.logger.log(user+' : Erm, Hello ?\n', 8)
    b(userData, game)

def exec(game):
    userData = game.userdata.get()
    if(not userData):
        game.logger.log('Corrupt Data...',3)
        input('Press enter to exit.')
        sys.exit(1)

    game.logger.log('Loading Stage...',0)
    if(userData['levelPart'] == 'a' or userData['levelPart'] == '-'):
        a(userData, game)
    elif(userData['levelPart'] == 'b'):
        b(userData, game)
    elif(userData['levelPart'] == 'c'):
        c(userData, game)
    elif(userData['levelPart'] == 'd'):
        d(userData, game)
    time.sleep(0.5)
    game.logger.log('Cleared chapter 1, Cleared User Display',0)
    game.logger.log('Saving Data, do not exit the game',2)
    userData['lastPlayed'] = int(round(time.time() * 1000))
    userData['level'] = 2
    userData['levelPart'] = '-'
    game.logger.log('Init save thread...',0)
    _thread.start_new_thread( game.userdata.set, (userData, game,) ) # multi-thread
    if(game.travis):
        return #only test 1 chapter for now
    game.logger.log('Save complete, would you like to end the game for today or move onto chapter 2 ?',1)
    i = input('Quit ? (yes/no) > ').lower()
    if(i[0] == 'y'):
        sys.exit(0) #status code 0- normal.
    time.sleep(1)
    input('Press enter to continue..')
    print('\x1b[2J')
    game.logger.log('Chapter 1 ended',0)
    #finish chapter
