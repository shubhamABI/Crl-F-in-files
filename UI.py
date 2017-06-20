#from tkinter import Tk, Label, Button
#
#class MyFirstGUI:
#    def __init__(self, master):
#        self.master = master
#        master.title("A simple GUI")
#
#        self.label = Label(master, text="This is our first GUI!")
#        self.label.pack()
#
#        self.greet_button = Button(master, text="Greet", command=self.greet)
#        self.greet_button.pack()
#
#        self.close_button = Button(master, text="Close", command=master.quit)
#        self.close_button.pack()
#
#    def greet(self):
#        print("Greetings!")
#
#root = Tk()
#my_gui = MyFirstGUI(root)
#root.mainloop()


import tkinter
from tkinter import *


root = Tk()
root.title('Random')
x = Label(text='How many squares? (ex: 4x4, 5x3)').pack(side=TOP,padx=10,pady=10)
Entry(root, width=10).pack(side=TOP,padx=10,pady=10)
Button(root, text='OK').pack(side= LEFT)
Button(root, text='CLOSE' ).pack(side= RIGHT)
root.mainloop()