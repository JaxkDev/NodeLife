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
# Copyright (C) 2018 Jackthehack21

# This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or any later version.

# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  

# See the GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  
# If not, see https://www.gnu.org/licenses/

import os, sys, time, importlib, threading, random

def test():
    id = str(random.randint(1000,5000))
    print('start - '+id)
    time.sleep(random.randint(0,5))
    print('end - '+id)
    return

class manager:
    def __init__(self, game):
        self.game = game
        self._idCount = 1000
        self._threads = {}
        self._active = threading.active_count()
        self._limit = 5 #Todo: config here (2 is from system, 1 is thread handler, 1 is sound manager, leaves 1 spaces for others.)
                        #Note: SockThread is found when running from IDE

        self.game.logger.log('[ThreadMgr] : System starting...',0)
        
        self.game.logger.log('[ThreadMgr] : Handler Spawning... ('+str(threading.active_count())+' threads running)',0)
        threading.Thread(
            name="ThreadingManager",
            target=self.handler,
            daemon=True
        ).start()
        self.game.logger.log('[ThreadMgr] : Handler Spawned. ('+str(threading.active_count())+' threads running)',0)
        running = list()
        for thread in threading.enumerate():
            running.append(thread.name)
        self.game.logger.log('[ThreadMgr] : Threads running = '+','.join(running),0)
    def add(self, thread, args=(), name="Child Thread #{ID}"):
        self._idCount += 1
        ID = str(self._idCount)
        self.game.logger.log('[ThreadMgr] : Thread added to list with ID: '+ID,0)
        self._threads[ID] = threading.Thread(
            name=name.replace('{ID}',ID),
            target=thread,
            args=args,
            daemon=True
        )
        self._threads[ID].started = False

    def run(self, ID):
        self._threads[ID].start()
        self._threads[ID].started = True
        #print(self._threads[ID].started)
        self.game.logger.log('[ThreadMgr] : Thread started = #'+ID,0)

    def handler(self):
        #for i in range(50):
        #    self.add(test)  #test successful !
        while(True):
            time.sleep(0.2) # 5 ticks per second (TODO: CONFIG)
            self._active = threading.active_count()
            threads = []
            for thread in threading.enumerate(): 
                if(thread.name != 'MainThread' and thread.name != 'ThreadingManager' and thread.name != 'SoundManager'):
                    threads.append(thread.name)
            keys = list()
            for i in self._threads.keys():
                keys.append(i)
            i = 0
            while(i < len(keys)):
                obj = self._threads[keys[i]]
                if(obj.started == True and obj.isAlive() == False):
                    self.game.logger.log('[ThreadMgr] : Thread removed = #'+keys[i],0)
                    del self._threads[keys[i]]
                i +=1
            self._active = threading.active_count()
            keys = list()
            for i in self._threads.keys():
                keys.append(i)
            if(self._active > self._limit):
                #Should never happen...
                self.game.logger.log('[ThreadMgr] : THREAD LIMIT EXCEEDED ! ('+str(threading.active_count())+')',3)
            else:
                i = 0
                i2 = 0
                while(i < self._limit-self._active and len(keys) > i2):
                    try:
                        if(self._threads[keys[i2]].started == True):
                            i2 += 1
                            continue
                        else:
                            self.run(keys[i2])
                            i2 += 1
                            i += 1
                    except IndexError:
                        self.game.logger.log('[ThreadMgr] : Error Occured (Index error L107 in threadmgr)',3)
