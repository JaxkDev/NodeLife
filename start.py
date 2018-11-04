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

from system.utils import logger
import time, platform, os, sys, system.ver
from system import preboot
from system.utils.initialise import init
from system.network import autoUpdate
init() #ENABLES COLOUR (WRAPS STDOUT & ERR) for windows.

tested_OS = ['darwin','linux','windows']
tested_ARM = ['amd64', 'x64', 'x86_64']

def pr(msg, lvl):
    logger.log(msg, lvl)

pr('Booted on '+time.asctime(), 0)
import ctypes
try:
    sys.stdout.write("\x1b]2;NodeLife: Will you survive ?\x07") # <-- works on all 3 osx,linux,win
    # windows only --> ctypes.windll.kernel32.SetConsoleTitleW("NodeLife: Will you survive ?")
    pr('Updated screen title',0)
except AttributeError:
    pr('Unable to set title',0) #Please open issue if you get this !
pr('Checking deployment type...',0)
if(not system.ver.release()):
    pr('Your running a development build, instead of a release please be aware this build has issues and if you dont know why your seeing this get a release from\nhttps://github.com/Jackthehack21/NodeLife/releases\n', 2)
    input('Press enter to continue.\n')
else:
    pr('running released version',0)
pr('Checking System...', 1)
time.sleep(0.5)
system = platform.uname()
if(not system.system.lower() in tested_OS):
    pr('Your system \''+system.system+'\' has not been tested, if you find issues please report them to our github page <https://github.com/Jackthehack21/NodeLife)', 2)
if(not system.machine.lower() in tested_ARM):
    pr('Your CPU running \''+system.machine+'\' has not been tested, if you find issues please report them to our github page <https://github.com/Jackthehack21/NodeLife)', 2)
if(int(os.path.getsize('data/logs/log.txt')/1024) >= 2024):
    pr('Your Log.txt (data/logs/log.txt) is extremely large >2mb and should not be that large, if you have experienced no problems please type D and press enter, and we will delete it for you, otherwise just press enter.', 3)
    if(input('> ').lower() == 'd'):
        time.sleep(0.5) #let logger finish anything not finished
        os.remove('data/logs/log.txt')
        pr('Log Wiped',2) #Use this to re-create the file aswell
        time.sleep(0.5)
elif(int(os.path.getsize('data/logs/log.txt')/1024) >= 1024):
    pr('Your Log.txt (data/logs/log.txt) is very large >1mb and should not be that large, if you have experienced no problems please type D and press enter, and we will delete it for you, otherwise just press enter.', 2)
    if(input('> ').lower() == 'd'):
        time.sleep(0.5) #let logger finish anything not finished
        os.remove('data/logs/log.txt')
        pr('Log Wiped',2) #Use this to re-create the file aswell
        time.sleep(0.5)
pr('System Check Complete.',0)
pr('Running preboot functions.',0)
preboot.run(False, system.system.lower())
pr('preboot, complete.',0)
pr('Checking for updates...', 1)
autoUpdate.check(False)
pr('Update Check Complete.',0)
pr('Starting Game...', 1)
time.sleep(3)
print('\x1b[2J')

from system import boot
boot.run(False)
pr('Game ended.',0)