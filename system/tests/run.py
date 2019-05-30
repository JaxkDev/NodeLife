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

import sys
import time
from traceback import format_exception

from system import boot
from system import game as gameobject
from system import preboot
from system.network import autoUpdate, postError, checkNotices
from system.utils.initialise import init

init()  # ENABLES COLOUR (WRAPS STDOUT & ERR) for windows 10.

tested_OS = ['darwin', 'linux', 'windows']
tested_ARM = ['amd64', 'x64', 'x86_64']


def excepthook(type_, value, traceback):
    game.logger.log(''.join(format_exception(type_, value, traceback)), 2)
    error = format_exception(type_, value, traceback)
    contact = 'TRAVIS'
    postError.exec([error, contact], game)


game = gameobject.Game(True)
game.logger.log('Booted on '+time.asctime(), 0)
try:
    sys.stdout.write("\x1b]2;NodeLife: Will you survive ?\x07")  # <-- works on all 3 osx,linux,win except travis
    game.logger.log('Updated screen title', 0)
except AttributeError:
    game.logger.log('Unable to set title', 0)  # Please open issue if you get this !
game.logger.log('Checking deployment type...', 0)
if not game.build.release():
    game.logger.log('Your running a development build, instead of a release please be aware this build has issues and '
                    'if you dont know why your seeing this get a release '
                    'from\nhttps://github.com/Jackthehack21/NodeLife/releases\n', 2)
else:
    game.logger.log('running released version', 0)

game.logger.log('Setting sys vars', 0)
sys.excepthook = excepthook
game.logger.log('Set sys vars !', 0)
game.logger.log('Checking System...', 1)
system = game.os
if not system.system.lower() in tested_OS:
    game.logger.log('Your system \''+system.system+'\' has not been tested, if you find issues please report them to '
                                                   'our github page <https://github.com/Jackthehack21/NodeLife)', 2)
if not system.machine.lower() in tested_ARM:
    game.logger.log('Your CPU running \''+system.machine+'\' has not been tested, if you find issues please report '
                                                         'them to our github page '
                                                         '<https://github.com/Jackthehack21/NodeLife)', 2)
game.logger.log('System Check Complete.', 0)
game.logger.log('Running preboot functions.', 0)
preboot.run(game)
game.logger.log('preboot, complete.', 0)
game.logger.log('Checking for updates...', 1)
autoUpdate.check(game)
game.logger.log('Update Check Complete.', 0)
game.logger.log('Checking for notices...', 1)
checkNotices.check(game)
game.logger.log('Notice Check Complete', 0)
game.logger.log('Starting Game...', 1)
time.sleep(3)
print('\x1b[2J')
boot.run(game)


game.logger.log('Game ended.', 0)
game.logger.log('-- testing logger --', 1)
game.logger.log('Log Msg', 1)
game.logger.log('Log Warning', 2)
game.logger.log('Log Error', 3)
game.logger.log('-- Tests ended --', 1)
