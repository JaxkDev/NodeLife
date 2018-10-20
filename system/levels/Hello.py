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

# CHAPTER 1 - HELLO ?
#
# tHE USER WILL LEARN WHAT IS HAPPENING AND GET TO KNOW THE UI.

#pylint: disable=W0612
#Stupid rule

import sys, time

def exec(pr, Travis):
    sys.stdout.write('\033[35m')
    for i in 'INCOMING TRANSMISSION':
        sys.stdout.write(i)
        time.sleep(0.05)
    for i in range(6):
        sys.stdout.write('.')
        time.sleep(0.6)
    sys.stdout.write('.\n\n')
    time.sleep(1.5)
    sys.stdout.write('CONNECTION ESTABLISHED.\033[39m\n\n\n')
    time.sleep(0.5)
    pr('Ugh, Maybe one day they\'ll send someone to fetch my body...\n',5)
    if(Travis):
        pr('TESTS ENDED.',2)
        return
    response = ''
    while(True):
        pr('\nOption A:  Hello ?\nOption B:  Hi there Mike !\n', 6)
        i = input('Type a option: ').lower()
        sys.stdout.write('\n')
        if(i == 'a' or i == 'b'):
            response = i
            break
    if(i == 'a'):
        pr('Hello !!????\nWas that someone ???\n',5)
        pr('Yes, Hello ?\n', 8)
    else:
        pr('Yes, Yes i knew i wasnt alone i knew someone would rescue me !\n', 5)
        time.sleep(1)
        pr('Of course they sent someone, why wouldnt they !\n', 5)
        time.sleep(1)
        pr('Erm, Hello ?\n', 8)
    time.sleep(0.5)
    pr('Ah yes of course sorry where\'s my manners, My name is \"Mike\"', 5)

        
