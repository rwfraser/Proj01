# GUI Widgets etc.  
#  fixes:  fix initial window size,  make bind functions work for default keystrokes such as ctrl-x to quit, and <enter> on bell button, create status window with updates
#  add drop down menus, add various bell sounds,catch premature shutdown error
# add mypy, pylint libraries to improve code quality
# add unittesting to be sure 100% code paths are tested

import sys
import typing
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from calendar import month_name 
root=Tk()
c = ttk.Frame(root, padding=(5, 5, 12, 0))
c.grid(column=0, row=0, sticky=(N,W,E,S))
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(0,weight=1)
# set default initial window size
WHeight = 350
WWidth = 350


def DescMouseActions(WWidth: int, WHeight: int) -> None:
	root.title('Mouse Events')
	m =ttk.Label(root, text="Starting...")
	m.grid(column=0, row=1)
	m.bind('<Enter>', lambda e: m.configure(text='Moved mouse inside'))
	m.bind('<Leave>', lambda e: m.configure(text='Moved mouse outside'))
	m.bind('<1>', lambda e: m.configure(text='Clicked left mouse button'))
	m.bind('<Double-1>', lambda e: m.configure(text='Double clicked'))
	m.bind('<B3-Motion>', lambda e: m.configure(text='right button drag to %d,%d' % (e.x, e.y)))

def DoSomeLabels():
	root.title('Labels')
	l =ttk.Label(root, text="Labels Section...", foreground='red', background='blue', anchor='e', justify='center')
	l.grid(column=0, row=2, sticky=(N,W,E,S))

def DoSomeButtons():
	root.title('Buttons...')
	b= ttk.Button(root, text='Push Me', command=beep, default = 'active')
	b.grid(column=0, row=3, sticky=(S,E,W,N))


def checkbutton(WhatsitStatus):
	root.title('Toggle Whatsit')
	# Whatsit is not initialized properly
	cb = ttk.Checkbutton(root, text = 'Use Whatsit?', variable=WhatsitStatus, onvalue= 'True', offvalue='False')
	cb.grid(column= 0, row = 4)

def radiobutton():
	root.title('Make A Choice')
	radiochoice = StringVar()
	rb1 = ttk.Radiobutton(root, text='Choice 1', variable = radiochoice, value='One')
	rb2 = ttk.Radiobutton(root, text = 'Choice 2', variable = radiochoice, value ='Two')
	rb3 = ttk.Radiobutton(root, text = 'Choice 3', variable = radiochoice, value = 'Three')
	rb1.grid(column= 0, row = 5)
	rb2.grid(column= 0, row = 6)
	rb3.grid(column= 0, row = 7)


def entryfield():
	root.title("Data Entry Field")
	# by default Entry fields are not labelled 
	EntryVar = StringVar()
	EntryVarField = ttk.Entry(root, textvariable = EntryVar)
	EntryVarField.grid(column = 0, row = 8)

def passwordfield():
	root.title("Password entry")
	PassVar = StringVar()
	PassVarField = ttk.Entry(root, textvariable = PassVar, show = '*')
	PassVarField.grid(column = 0, row = 9)

def mycombobox():
	root.title('My Combo Box')
	ComboVar = StringVar()
	mycombobx = ttk.Combobox(root, textvariable = ComboVar)
	mycombobx['values'] = ('Bigfork','Kalispell', 'Whitefish')
	mycombobx.grid(column = 0, row = 10)


def lbox():
	root.title('Listbox:')
	choices = ['jan', 'feb','mar']
	'''
	choices = ''
	for m in month_name:
		choices = choices + m + ','
	choices = choices[:-1]
	'''
	choicesvar = StringVar(value=choices)
	lb = Listbox(root, height = 5, listvariable = choicesvar)
	lb.grid(column = 2, row = 1, rowspan = 4)


def QuitButton():
	root.title('Exit')
	x = ttk.Button(root, text='Quit', command=finish, default='normal')
	x.grid(column=2, row=11)
	return  True
#	root.bind('<Return>', x.invoke())


def beep():
	root.bell()

def finish() -> bool:
	exit()

def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.destroy()
        finish()


ExitVar = False

while  not ExitVar:
	
	# exit if Window frame 'X' is clicked
	root.protocol("WM_DELETE_WINDOW", on_closing)
	# throws EOF error ?
	x= input('any key to see Listbox')
	lbox()
	x= input('any key to see Mouse Movements')
	DescMouseActions(WWidth, WHeight)
	x = input('any key to see labels')
	DoSomeLabels()
	x = input('any key to see buttons')
	DoSomeButtons()
	WhatsitStatus= True
	x = input('any key to see Whatsit Toggle')
	checkbutton(WhatsitStatus)
	x = input('any key to see Radio Button')
	radiobutton()
	x = input('any key to see Entry Field')
	entryfield()
	x = input('any key to see Password Field')
	passwordfield()
	x = input('any key to see MyComboBox')
	mycombobox()
	x = input('any key to see Exit Button')
	ExitVar = QuitButton()
	root.mainloop()
