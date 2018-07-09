import tkinter as tk  #assigning tkinter a small name-tk for writeability
import backend
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import numpy as np   #similary importing numpy as np (renaming)
import sys
#########################- Button commands -################################################

def view_all():
	
	pass	
def search():	
	pass
def add():
	pass
def update():
	pass
def delete():
	pass
def close():	
	result=messagebox.askyesno('Exit confirmation dialogue box','Are you sure want to close')
	if result==True:
		sys.exit()
	else:
		pass	
def match():
	pass
########################################################################################################	
# login=tk.Tk()
# login.title("Database login", font=('arial', 15))
# login.geometry('230x150')
# Label(login,text="Enter here").grid(sticky=E)
# Label(login,text="Username\t").grid(row=1,column=0)
# Label(login,text="Password\t").grid(row=2,column=0)
# username_entry=Entry(login).grid(row=1,column=1)
# password_entry=Entry(login,show='*').grid(row=2,column=1)
# login_bt=tk.Button(login,text="\tlogin \t",bg='powder blue',command=match)
# login_bt.grid(row=4,column=1)

############################################################################################################

#window configuration
window=tk.Tk()
window.title("Book Dictionary")
window.geometry('350x250')
window.resizable(width=FALSE,height=FALSE)

#frames configuration
upframe=Frame(window)
upframe.place()

downframe=Frame(window)
downframe.place(x=10,y=50)
##############################-Label and Entries-##########################################################

Label(window,text="Title\t").grid(row=0,column=0)

title_entry=Entry(window)
title_entry.grid(row=0,column=1)
title=title_entry.get()

Label(window,text="Author").grid(row=0,column=2)

author_entry=Entry(window)
author_entry.grid(row=0,column=3)

Label(window,text="Year\t").grid(row=1,column=0)
title_entry=Entry(window)
title_entry.grid(row=1,column=1)

Label(window,text="ISBN").grid(row=1,column=2)

author_entry=Entry(window)
author_entry.grid(row=1,column=3)


# from tkinter import scrolledtext
main_list=scrolledtext.ScrolledText(downframe,width=21,height=10)
main_list.grid(row=4,column=0)
# main_list.insert(INSERT,'Hi !')
# main_list.delete(1.0,END)

#########################= Buttons layout -################################################
view_all_bt=tk.Button(window,text='View All',width=15,command=view_all)
view_all_bt.grid(row=3,column=3)

search_bt=tk.Button(window,text='Search Entry',width=15,command=search)
search_bt.grid(row=4,column=3)

add_bt=tk.Button(window,text='Add Entry',width=15,command=add)
add_bt.grid(row=5,column=3)

update_bt=tk.Button(window,text='Update Selected',width=15,command=update)
update_bt.grid(row=6,column=3)

delete_bt=tk.Button(window,text='Delete Selected',width=15,command=delete)
delete_bt.grid(row=7,column=3)

close_bt=Button(window,text='Close',command=close,width=15)
close_bt.grid(row=8,column=3)
########################################################################
window.mainloop()