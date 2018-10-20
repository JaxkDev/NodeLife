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
import os, sys, time, platform

from system.utils.initialise import init
from system.network import autoUpdate
init() #ENABLES COLOUR (WRAPS STDOUT & ERR)

def pr(msg, lvl):
    logger.log(msg, lvl)

pr('Booted on '+time.asctime(), 0)
pr('Checking System...', 1)
time.sleep(0.5)
system = platform.uname()
if(system.system.lower() != 'windows'):
    pr('Your system \''+system.system+'\' has not been tested, if you find issues please report them to our github page <https://github.com/Jackthehaxk21/NodeLife)', 2)
if(system.machine.lower() != 'amd64'):
    pr('Your CPU running \''+system.machine+'\' has not been tested, if you find issues please report them to our github page <https://github.com/Jackthehaxk21/NodeLife)', 2)

pr('System Check Complete.',0)
pr('Checking for updates...', 1)
autoUpdate.check()
pr('Update Check Complete.',0)
pr('Starting Game...', 1)
time.sleep(3)
print('\x1b[2J')
from system import boot
boot.run(True)