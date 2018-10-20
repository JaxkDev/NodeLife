import sys, os

def log(msg, lvl):
    sav(msg, lvl)
    if(lvl >= 1 and lvl < 3):
        sys.stdout.write(msg+'\n')
    elif(lvl >= 3):
        sys.stderr.write(msg+'\n')
    return

def sav(msg, lvl):
    if not os.path.exists('data'):
        os.makedirs('data')
    f = open('data/log.txt', 'a')
    f.write(msg+'\n')
    f.close()