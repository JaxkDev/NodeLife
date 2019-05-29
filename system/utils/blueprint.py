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

# pylint: disable=W0101
# For now as i return and have code after it


def spawn():
    # guess i could add 2.x support here...
    try:
        import tkinter as tk
    except ImportError:
        import Tkinter as tk

    import random
    import sys
    import os
    from tkinter import messagebox
    script_dir = sys.path[0]
    img_path = os.path.join(script_dir, '../resources/map.png')
    ico_path = os.path.join(script_dir, '../resources/icon.png')

    root = tk.Tk()
    root.resizable(False, False)
    # noinspection PyProtectedMember
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=ico_path))
    root.title('Transmission_ID:'+str(random.randint(9999, 99999)))
    widget = tk.Label(root, compound='top')
    widget.lenna_image_png = tk.PhotoImage(file=img_path)
    widget['text'] = "Crystal Blueprints"
    widget['image'] = widget.lenna_image_png
    widget.pack()

    def on_closing():
        if messagebox.askokcancel("Exit", "Do you want to close this transmission?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
