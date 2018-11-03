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

import sys, os, time, platform

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

def log(msg, lvl = 5):
    sav(msg, lvl)
    if(lvl == 1):
        #log/output
        sys.stdout.write(msg+'\n')
    elif(lvl == 2):
        #warning
        sys.stdout.write('\x1b[1m\033[33m[WARNING] : '+msg+'\033[39m\x1b[21m\n')
    elif(lvl == 3):
        #error
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
