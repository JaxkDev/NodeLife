
def exec():
    try:
        import tkinter as tk
    except ImportError:
        import Tkinter as tk

    import random, sys, os
    from tkinter import messagebox
    script_dir = sys.path[0]
    img_path = os.path.join(script_dir, '../resources/map.png')
    ico_path = os.path.join(script_dir, '../resources/icon.png')

    root = tk.Tk()
    root.resizable(False, False)
    root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file=ico_path))
    root.title('Transmission_'+str(random.randint(9999,99999)))
    widget = tk.Label(root, compound='top')
    widget.lenna_image_png = tk.PhotoImage(file=img_path)
    widget['text'] = "Crystal Blueprints"
    widget['image'] = widget.lenna_image_png
    widget.pack()
    def on_closing():
        return #for now not allowed to close.
        if messagebox.askokcancel("Delete", "Do you want to delete the transmission?"):
            root.destroy()

    root.protocol("WM_DELETE_WINDOW", on_closing)
    root.mainloop()
