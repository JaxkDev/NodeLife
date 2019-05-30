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
import os
import random
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
tested_ARM = ['amd64', 'x64', 'x86_64', 'armv7l']


# Todo, make this a separate thread that listens for event finished to return back to Main thread
# so it actually loads the game as its playing the animation, also find another loading bar ascii method
# current one is laggy as it clears whole screen instead of one line.
def welcome():
    top = "\x1b[2J"+(" "*30)+"\x1b[1m\033[33mLoading NodeLife \x1b[1m\033[36mv"+game.build.ver() + \
          "\n\033[39m\x1b[21m+------------------------------------------------------------------------------+"

    bot = "\n+------------------------------------------------------------------------------+"

    x = 0
    max = 78

    mover = "\x1b[1m\033[91m███████\033[39m\x1b[21m"

    count = random.randint(50, 500)

    while count >= 0:
        time.sleep(0.1)
        if x >= max-7:
            x = 0
        bar = "\n|"+str(" "*((max+x)-max))+mover+str(" "*(max-(x+7)))+"|"
        all = top+bar+bot
        sys.stdout.write(all)
        # So i clear screen instead
        # sys.stdout.write("\r") Issue is changing screen size causes a lot of issues visually.
        # sys.stdout.write("\u001B[3A")  # move cursor 3 positions up (to over write loading bar)
        x += 1
        count -= 1


def excepthook(type_, value, traceback):
    if type_.__name__ == "KeyboardInterrupt":
        game.logger.log("KeyboardInterrupt caught, exiting with status code 1", 2)
        sys.exit(1)
    game.logger.log(''.join(format_exception(type_, value, traceback)), 2)
    error = format_exception(type_, value, traceback)
    if not game.travis:
        contact = input('The following error occurred, and has been sent to me, please type a way of contacting you so '
                        'i can get in touch ! :')
    else:
        contact = 'Travis'
    postError.exec([error, contact], game)


game = gameobject.Game(False)
game.logger.log('Booted on ' + time.asctime(), 0)
sys.stdout.write("\x1b]2;NodeLife: Will you survive ?\x07")  # <-- works on all 3 osx,linux,win except travis
game.logger.log('Checking deployment type...', 0)
if not game.build.release():
    game.logger.log('Your running a development build, instead of a release please be aware this build has issues and '
                    'if you dont know why your seeing this get a release '
                    'from\nhttps://github.com/Jackthehack21/NodeLife/releases\n', 2)
    input('press enter to continue.\n')
else:
    game.logger.log('running released version', 0)

game.logger.log('Setting sys vars', 0)
sys.excepthook = excepthook
game.logger.log('Set sys vars !', 0)
game.logger.log('Checking System...', 1)

system = game.os
if not system.system.lower() in tested_OS:
    game.logger.log(
        'Your system \'' + system.system + '\' has not been tested, if you find issues please report them to '
                                           'our github page <https://github.com/Jackthehack21/NodeLife)', 2)
if not system.machine.lower() in tested_ARM:
    game.logger.log('Your CPU running \'' + system.machine + '\' has not been tested, if you find issues please report '
                    'them to our github page <https://github.com/Jackthehack21/NodeLife)', 2)
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

while True:  # cheeky me :)
    time.sleep(0.2)
    try:
        columns, rows = os.get_terminal_size(0)
    except OSError:
        columns, rows = os.get_terminal_size(1)
    if columns < 100 or rows < 20:
        sys.stdout.write("\x1b[2J[Warning] : Please change your screen "  # Ready for the sexy loading bar...
                         "size to at least 100x20, its currently: "+str(columns)+"x"+str(rows))
    else:
        print("\x1b[2J")
        break

welcome()
print("\x1b[2J")

#############################
# START LEVELS.

boot.run(game)
# RETURNS WHEN FINISHED.
#############################

game.logger.log('Game ended.', 0)

# TODO: Wait for threading tasks to complete instead of killing them with spawn.
