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

# CHAPTER 0 - Introduction
#
# THE USER WILL LEARN WHAT THIS GAME IS.

#pylint: disable=W0612
#Stupid rule

import sys, time, random, os, system.utils.username, _thread
import system.utils.userdata as userdata

def slow(txt, delay):
    for i in txt:
        sys.stdout.write(i)
        time.sleep(delay)

def a(user, pr, Travis):
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
    input('Press enter to start the game !')

def exec(userData, pr, Travis):
    if(userData != {}):
        pr('Corrupt Data found, please delete the data/user folder.',3)
        input('Press enter to continue...')
        sys.exit(1)
    a(userData, pr, Travis)
    pr('Saving game...',1)
    user = '['+system.utils.username.Username()+']' #Fix for linux and mac users. To be added to userData
    userData['username'] = user
    userData['lastPlayed'] = int(round(time.time() * 1000))
    userData['level'] = 1
    userData['levelPart'] = '-'
    pr('Init save thread...',0)
    userdata.set(userData, pr)