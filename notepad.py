import tkinter as tk
def red_colour():
    my_window['bg']='red'
def green_colour():
    my_window['bg']='green'
def blue_colour():
    my_window['bg']='blue'
def White_colour():
    my_window['bg']='white'

my_window=tk.Tk()
my_menubar=tk.Menu(my_window)
my_dropdown_menu=tk.Menu(my_menubar,tearoff=0)
my_dropdown_menu.add_command(label='red',command=red_colour)
my_dropdown_menu.add_command(label='green',command=green_colour)
my_dropdown_menu.add_command(label='blue',command=blue_colour)
my_dropdown_menu.add_command(label='white',command=White_colour)
my_menubar.add_cascade(label='colour',menu=my_dropdown_menu)
my_window.config(menu=my_menubar)
my_window.mainloop()


