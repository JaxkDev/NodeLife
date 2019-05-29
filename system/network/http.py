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

import math
import sys
from urllib import request, error, parse

# noinspection PyBroadException
try:
    # noinspection PyUnresolvedReferences
    import httplib
except:
    import http.client as httplib


def progressbar(chunk, chunk_size, total_size):
    percent = math.floor((100/total_size)*(chunk_size*chunk))  # note it may go above 100 for last chunk.
    if percent > 100:
        percent = 100
    bars = ("█"*math.floor(percent/5))+(" "*(20-math.floor(percent/5)))
    sys.stdout.write("\r")
    sys.stdout.write("[%s] %d/100 Downloading..." % (bars, percent))
    # sys.stdout.flush()


def valid_connection():
    conn = httplib.HTTPConnection("www.google.com", timeout=5)
    # noinspection PyBroadException
    try:
        conn.request("HEAD", "/")
        conn.close()
        return True
    except:
        conn.close()
        return False


def get(url, game):
    try:
        resp = request.urlopen(url)
    except error.HTTPError:
        game.logger.log('HTTP GET request to \''+url+'\' returned a error or crashed.', 3)
        resp = False
    return resp


def post(url, data, game):
    data = parse.urlencode(data).encode()
    req = request.Request(url, data=data)
    try:
        resp = request.urlopen(req)
    except error.HTTPError:
        game.logger.log('HTTP POST request to \''+url+'\' returned a error or crashed.', 3)
        resp = False
    return resp


def download(url, path, game, progress=True):
    try:
        if progress:
            request.urlretrieve(url, path, progressbar)
            print("Done")
        else:
            request.urlretrieve(url, path)
        return 0
    except error.HTTPError:
        game.logger.log('Failed to download.', 3)
        return 1
