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

from system.utils import logger
import time, platform, system.ver, os, sys

from system.utils.initialise import init
from system.network import autoUpdate
init() #ENABLES COLOUR (WRAPS STDOUT & ERR)

def pr(msg, lvl):
    logger.log(msg, lvl)

pr('Booted on '+time.asctime(), 0)
import ctypes
ctypes.windll.kernel32.SetConsoleTitleW("NodeLife: Will you survive ?")
pr('Updated screen title',0)
pr('Checking deployment type...',0)
if(not system.ver.release()):
    pr('Your running a development build, instead of a release please be aware this build has issues and if you dont know why your seeing this get a release from\nhttps://github.com/Jackthehack21/NodeLife/releases\n', 2)
    input('Press enter to continue.\n')
else:
    pr('running released version',0)
pr('Checking System...', 1)
time.sleep(0.5)
system = platform.uname()
if(system.system.lower() != 'windows'):
    pr('Your system \''+system.system+'\' has not been tested, if you find issues please report them to our github page <https://github.com/Jackthehaxk21/NodeLife)', 2)
if(system.machine.lower() != 'amd64' and system.machine.lower() != 'x64'):
    pr('Your CPU running \''+system.machine+'\' has not been tested, if you find issues please report them to our github page <https://github.com/Jackthehaxk21/NodeLife)', 2)
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
pr('Checking for updates...', 1)
autoUpdate.check(False)
pr('Update Check Complete.',0)
pr('Starting Game...', 1)
time.sleep(3)
print('\x1b[2J')

from system import boot
boot.run(False)
pr('Game ended.',0)
