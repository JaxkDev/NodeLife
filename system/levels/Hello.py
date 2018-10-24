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
# @author Jackthehack21 <gangnam253@gmail.com | Jackthehaxk21##860>
#
# This project and all its content is distributed under the GPL-V3 license

# CHAPTER 1 - HELLO ?
#
# THE USER WILL LEARN WHAT IS HAPPENING AND GET TO KNOW THE UI.

#pylint: disable=W0612
#Stupid rule

import sys, time, random, os, system.utils.username
import system.utils.userdata as userdata

def d(userData, pr, Travis):
    user = userData['username']
    time.sleep(0.5)
    pr(user+' : Whats the \'Crystal\' ?\n',8)
    time.sleep(0.5)
    pr('[Mike] : Oh right, sorry the \'Crystal\' is a space center, made to travel through space to planets and research them, we already gathered data from 3 of the 5 we were sent here to do but something happened in the lab...\n', 5)

def c(userData, pr, Travis):
    user = userData['username']
    time.sleep(0.5)
    pr(user+' : What Happened ?\n', 8)
    time.sleep(0.5)
    pr('[Mike] : Something happened in the lab and half of the Crystal is gone !\n', 5)
        
def b(userData, pr, Travis):
    user = userData['username']
    time.sleep(0.5)
    pr('[Mike] : Ah yes of course sorry where\'s my manners, My name is \"Mike\"\n', 5)
    time.sleep(0.5)
    pr('[Mike] : Im currently floating around on the Crystal, lost contact with humans about a week ago and almost gone through all of my rations...\n', 5)
    time.sleep(0.5)
    response = ''
    while(True):
        pr('\nOption A:  What Happened?\nOption B:  Whats the crystal?\nOption C:  Floating?\n', 6)
        if(Travis):
            response = random.choice(['a','b','c'])
            break
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if(i == 'a' or i == 'b' or i == 'c'):
            response = i
            break
    if(i == 'a'):
        c(userData, pr, Travis)
        #Whats the crystal ?
        d(userData, pr, Travis)
    elif(i == 'b'):
        d(userData, pr, Travis)
        #what happened ?
        c(userData, pr, Travis)
    else:
        pr(user+' : \'Floating\' ?\n',8)
        time.sleep(0.5)
        pr('[Mike] : Oops forgot to mention im in outer space in the crystal...', 5)
        #whats the crystal ?, what happened ?
        while(True):
            pr('\nOption A:  Whats the crystal ?\nOption B:  What happened?\n', 6)
            if(Travis):
                response = random.choice(['a','b'])
                break
            i = input('Type a option: ').lower()
            sys.stdout.write('\n')
            if(i == 'a' or i == 'b'):
                response = i
                break
        if(response == 'a'):
            d(userData, pr, Travis)
        else:
            c(userData, pr, Travis)
            

def a(userData, pr, Travis):
    user = userData['username']
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
    pr('[??] : Ugh, Maybe one day they\'ll send someone to fetch my body...\n',5)
    response = ''
    while(True):
        pr('\nOption A:  Hello ?\nOption B:  Hi there !\n', 6)
        if(Travis):
            response = random.choice(['a','b'])
            break
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if(i == 'a' or i == 'b'):
            response = i
            break
    if(i == 'a'):
        pr(user+' : Hello ?\n', 8)
        time.sleep(0.5)
        pr('[??] : Hello !!????\nWas that someone ???\n',5)
        time.sleep(0.5)
        pr(user+' : Yes, Hello ?\n', 8)
    else:
        pr(user+' : Hi there !\n',8)
        time.sleep(0.5)
        pr('[??] : Yes, Yes i knew i wasnt alone i knew someone would rescue me !\n', 5)
        time.sleep(0.5)
        pr('[??] : Of course they sent someone, why wouldnt they !\n', 5)
        time.sleep(0.5)
        pr(user+' : Erm, Hello ?\n', 8)
    b(userData, pr, Travis)

def exec(userData, pr, Travis):
    user = '['+system.utils.username.Username()+']' #Fix for linux and mac users. To be added to userData
    userData['username'] = user
    a(userData, pr, Travis)
    pr('Cleared chapter 1, Cleared User Display',0)
    pr('Saving Data, do not exit the game',2)
    #save data
    time.sleep(3)
    pr('Save complete, would you like to end the game for today or move onto chapter 2 ?',1)
    i = input('Quit ? (yes/no) > ').lower()
    if(i[0] == 'y'):
        sys.exit(0) #status code 0- normal.
    time.sleep('1')
    print('\x1b[2J')
    print('Chapter 2')
    input()
    #save data and finish chapter
