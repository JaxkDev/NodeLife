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
from system import ver
from urllib import request, error
import json

def check(travis):
    try:
        r = request.urlopen('https://fusioncraft.glitch.me/NodeLife?app='+ver.http())
    except error.HTTPError:
        logger.log('HTTP request to check for updates crashed.', 3)
        return
    if(r.status != 200):
        if(r.status >=400):
            logger.log('Failed to retrieve update information, error code: '+r.status+' Please create a issue on our github <https://github.com/Jackthehack21/NodeLife/issues>', 2)
        else:
            logger.log('Failed to retrieve update information, error code: '+r.status+' Please check your Internet Connection.', 2)
    logger.log('Sucessfully Got Update Information', 0)
    data = json.loads(r.read().decode("utf-8"))
    logger.log('Recieved Data from server: '+str(data), 0)
    if(update(ver.ver(), data['ver'])):
        logger.log('Update '+data['ver']+' is available at '+data['url'], 2)
        if(not travis):
            input('\nPress any key to continue...\n')
    else:
        logger.log('Game Up-To-Date !', 0)
    
    return

def update(n, n2):
    original = n.split('.')
    available = n2.split('.')
    if(int(original[0]) < int(available[0])):
        return True
    if(int(original[1]) < int(available[1])):
        return True
    if(int(original[2]) < int(available[2])):
        return True
    return False