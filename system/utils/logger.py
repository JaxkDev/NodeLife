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

import sys, os, time, platform
from system.network import postError

OS = platform.uname().system.lower()

data = {
    "0": "Debug",
    "1": "Log",
    "2": "Warning",
    "3": "Error",
    "4": "In-Game Notification",
    "5": "In-Game Message",
    "6": "In-Game Question",
    #7 UI
    "8": "User Response",
    "9": "Other"
}

from time import gmtime, strftime
def getTime():
    return strftime("%H:%M:%S", gmtime())

def logMsg(msg, game, lvl = 5):
    sav(msg, lvl)
    if(lvl == 1):
        #log/output
        sys.stdout.write(msg+'\n')
    elif(lvl == 2):
        #warning
        sys.stdout.write('\x1b[1m\033[33m[WARNING] : '+msg+'\033[39m\x1b[21m\n')
    elif(lvl == 3):
        #error
        postError.exec(msg,game)
        sys.stdout.write('\x1b[1m\033[91m[ERROR] : '+msg+'\033[39m\x1b[21m\n')
    elif(lvl == 4): 
        #In-Game Notification (e.g. system, asleep etc)
        sys.stdout.write('\033[97m')
        if(OS != "windows"):
            sys.stdout.write(msg)
        else:
            for i in msg:
                sys.stdout.write(i)
                time.sleep(0.09)
        sys.stdout.write('\033[39m\n')
    elif(lvl == 5): 
        #In-Game message
        sys.stdout.write('\033[36m')
        if(OS != "windows"):
            sys.stdout.write(msg)
        else:
            for i in msg:
                sys.stdout.write(i)
                time.sleep(0.09)
        sys.stdout.write('\033[39m\n')
    elif(lvl == 6): 
        #In-Game question
        sys.stdout.write('\033[32m[RESPOND] : ')
        if(OS != "windows"):
            sys.stdout.write(msg)
        else:
            for i in msg:
                sys.stdout.write(i)
                time.sleep(0.09)
        sys.stdout.write('\033[39m\n')
    elif(lvl == 8):
        #USER RESPONSE
        sys.stdout.write('\033[91m')
        if(OS != "windows"):
            sys.stdout.write(msg)
        else:
            for i in msg:
                sys.stdout.write(i)
                time.sleep(0.09)
        sys.stdout.write('\033[39m\n')
    elif(lvl == 9): 
        #Other
        sys.stdout.write(msg+'\n')

    return

def sav(msg, lvl):
    if not os.path.exists('data'):
        os.makedirs('data')
        os.makedirs('data/logs')
    elif not os.path.exists('data/logs'):
        os.makedirs('data/logs')
    f = open('data/logs/log.txt', 'a')
    f.write('['+getTime()+'] ['+data[str(lvl)]+'] '+msg.replace('\n',' ')+'\n')
    f.close()

class logger:
    def __init__(self, game):
        self.game = game
    
    def log(self,msg,lvl):
        logMsg(msg,self.game,lvl)