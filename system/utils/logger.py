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
# Copyright (C) 2019 Jackthehack21

# This program is free software: you can redistribute it and/or modify it under the terms of
# the GNU General Public License as published by the Free Software Foundation,
# either version 3 of the License, or any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.
# If not, see https://www.gnu.org/licenses/
import datetime
import inspect
import os
import platform
import sys
import time
from time import gmtime, strftime

from system.network import postError

OS = platform.uname().system.lower()

data = {
    "0": "Debug",
    "1": "Log",
    "2": "Warning",
    "3": "Error",
    "4": "In-Game Notification",  # dont log
    "5": "In-Game Message",  # dont log
    "6": "In-Game Question",  # dont log
    # 7 UI (dont log)
    "8": "User Response",  # dont log
    "9": "Other"  # dont log
}

speeds = {
    "veryslow": 0.2,
    "slow": 0.14,
    "normal": 0.09,
    "fast": 0.05,
    "insane": 0.01
}


def gettime():
    return strftime("%H:%M:%S", gmtime())


def logmsg(msg, game, lvl=5):
    if lvl < 4:
        sav(msg, lvl)
    if lvl == 0:
        return
    elif lvl == 1:
        # log/output
        sys.stdout.write(msg + '\n')
        return
    elif lvl == 2:
        # warning
        sys.stdout.write('\x1b[1m\033[33m[WARNING] : ' + msg + '\033[39m\x1b[21m\n')
        return
    elif lvl == 3:
        # error
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 0)
        for i in range(len(calframe)):  # Possibly use format_exception
            trace = "File: \"" + str(calframe[(len(calframe) - 1) - i][1]) \
                    + "\", Line: " + str(calframe[(len(calframe) - 1) - i][2]) + ", in function: " \
                    + str(calframe[(len(calframe) - 1) - i][3]) + "\n"  # Line too long :/
            sys.stdout.write('\x1b[1m\033[91m'+trace+'\033[39m\x1b[21m')
            sav(trace, 3)
        sys.stdout.write('\x1b[1m\033[91m[ERROR] : ' + msg + '\033[39m\x1b[21m\n')
        if not game.travis:
            contact = input(
                'The following error occurred, and will be sent to me, please type a way of contacting you so '
                'i can get in touch if needed to :')
        else:
            contact = 'Travis'
        postError.exec([msg, contact], game)
        time.sleep(3)
        sys.exit(1)
    cfg = game.config.get()
    user_name = cfg.get('General', 'userName')
    other_name = cfg.get('General', 'otherName')
    if lvl == 4:
        # In-Game Notification (e.g. system, asleep etc)
        msg = msg.replace("{NAME}", other_name)
        sys.stdout.write('\033[97m')
        if cfg.get("Graphics", "slow_text").lower() == "yes":
            for i in msg:
                sys.stdout.write(i)
                time.sleep(speeds[cfg.get("Graphics", "slow_text_speed").lower()])
        else:
            sys.stdout.write(msg)
        sys.stdout.write('\033[39m\n')
    elif lvl == 5:
        # In-Game message
        sys.stdout.write('\033[36m')
        if msg[0] != '[':  # hacky fix for starting of game where it is [??]
            msg = '[' + other_name + '] : ' + msg
        if cfg.get("Graphics", "slow_text").lower() == "yes":
            for i in msg:
                sys.stdout.write(i)
                time.sleep(speeds[cfg.get("Graphics", "slow_text_speed").lower()])
        else:
            sys.stdout.write(msg)
        sys.stdout.write('\033[39m\n')
    elif lvl == 6:
        # In-Game question
        sys.stdout.write('\033[32m[RESPOND] : ')
        if cfg.get("Graphics", "slow_text").lower() == "yes":
            for i in msg:
                sys.stdout.write(i)
                time.sleep(speeds[cfg.get("Graphics", "slow_text_speed").lower()])
        else:
            sys.stdout.write(msg)
        sys.stdout.write('\033[39m\n')
    elif lvl == 8:
        # USER RESPONSE
        sys.stdout.write('\033[91m')
        msg = '[' + user_name + '] : ' + msg
        if cfg.get("Graphics", "slow_text").lower() == "yes":
            for i in msg:
                sys.stdout.write(i)
                time.sleep(speeds[cfg.get("Graphics", "slow_text_speed").lower()])
        else:
            sys.stdout.write(msg)
        sys.stdout.write('\033[39m\n')
    elif lvl == 9:
        # Other
        sys.stdout.write(msg + '\n')

    return


def sav(msg, lvl):
    if not os.path.exists('data'):
        os.makedirs('data')
        os.makedirs('data/logs')
    elif not os.path.exists('data/logs'):
        os.makedirs('data/logs')
    date = datetime.datetime.now().strftime("%d.%m.%Y")
    f = open('data/logs/' + date + '.log', 'a')
    f.write('[' + gettime() + '] [' + data[str(lvl)] + '] ' + msg.replace('\n', ' ') + '\n')
    f.close()


class Logger:
    def __init__(self, game):
        self.game = game

    def log(self, msg, lvl):
        logmsg(msg, self.game, lvl)
