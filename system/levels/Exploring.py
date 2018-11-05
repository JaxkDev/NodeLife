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

import sys, time, random, os, _thread
import system.utils.userdata as userdata

def slow(txt, delay):
    if(platform.uname().system.lower() != "windows"):
        sys.stdout.write(txt)
        return
    for i in txt:
        sys.stdout.write(i)
        time.sleep(delay)


def save(userData, levelPart, pr):
    userData['lastPlayed'] = int(round(time.time() * 1000))
    userData['levelPart'] = levelPart
    pr('Init save thread...',0)
    _thread.start_new_thread( userdata.set, (userData, pr,) ) # multi-thread


def c(user, pr, Travis):
    save(user,"c",pr)
    pr("c",0)

def b(user, pr, Travis):
    save(user,"b",pr)
    pr("b",0)

def a(user, pr, Travis):
    save(user,"a",pr)
    pr("a",0)

def exec(userData, pr, Travis):
    if(userData == {}):
        pr('Corrupt Data found, please delete the data/user folder.',3)
        input('Press enter to continue...')
        sys.exit(1)
    a(userData, pr, Travis)
    pr('Saving game...',1)
    userData['lastPlayed'] = int(round(time.time() * 1000))
    userData['level'] = 3
    userData['levelPart'] = '-'
    pr('Init save function...',0)
    userdata.set(userData, pr)
