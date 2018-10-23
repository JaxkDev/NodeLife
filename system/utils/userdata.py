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

import os, sys, json
import system.utils.secure as sec

def get():
    #Get user data
    if(not os.path.exists('data/')):
        os.mkdir('data')
        return
    if(not os.path.exists('data/user/')):
        os.mkdir('data/user')
        return
    if(not os.path.isfile('data/user/data.secure')):
        return
    
    f = open('data/user/data.secure', 'r')
    #decode data (f.read())
    data = json.loads(f.read()) #do json after decode when implemented
    f.close()
    print(data)

def set(data):
    #Set user data
    if(not os.path.exists('data/')):
        os.mkdir('data')
        return
    if(not os.path.exists('data/user/')):
        os.mkdir('data/user')
        return
    #encode data
    f = open('data/user/data.secure', 'w')
    f.write(json.dumps(data)) #do json before encode when implemented
    f.close()
    return