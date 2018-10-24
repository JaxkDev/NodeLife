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

from system.utils import logger, userdata
import time, os
from system.levels import Hello
import importlib

def pr(msg, lvl):
    logger.log(msg, lvl)

levels = {
    "1": importlib.import_module("system.levels.Hello")
}

def run(Travis):
    if(Travis):
        pr('Skipped save check.',0)
        pr('Travis Mode Enabled',2)
        levels['1'].exec({}, pr, True)
        return
    pr('Checking for saves',0)
    userData = userdata.get()
    if(userData != {}):
        print('TBC - SAVES')
        #go back to where he came from, using levels var
    else:
        pr('No saves found.', 0)
        pr('Loading Chapter 1', 0)
        levels['1'].exec(userData, pr, False)
