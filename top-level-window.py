from tkinter import *
from tkinter import ttk

root = Tk()
frame = ttk.Frame(root)

frame.pack()

frame.config(height=200, width= 400)
frame.config(relief= RIDGE)

ttk.Button(frame, text='click me').grid()
frame.config(padding = (30, 50))
ttk.LabelFrame(root, height = 100, width=200, text='MyFrame').pack()

window = Toplevel(root)
window.title('New Window')

window.geometry('640x480+50+100')

# prevent user from resizing

window.resizable(True, True)

#limit allowable resize of windows
window.maxsize(640, 480)
window.minsize(200, 200)



if __name__ == '__main__':
    mainloop()