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
init() #ENABLES COLOUR (WRAPS STDOUT & ERR)

def pr(msg, lvl):
    logger.log(msg, lvl)

print('\033[31m HI')
pr('Booted on '+time.asctime(), 0)
pr('Checking System...', 1)
time.sleep(0.5)
system = platform.uname()
if(system.system != 'Windows'):
    pr('Your system \''+system.system+'\' has not been tested, if you find issues please report bugs to our github page <https://github.com/Jackthehack21/NodeLife)', 2)

