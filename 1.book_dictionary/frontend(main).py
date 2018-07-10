import tkinter as tk  #assigning tkinter a small name-tk for writeability
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import sys

def view_all():
	# for row in backend.view_alll():
	# main_list.grid(row=4,column=0)
		# main_list.insert(1,'row')
	# main_list.delete(1.0,END)
	import backend
	listing.delete(0,END)
	for row in backend.view_alll():
		listing.insert(END,row)

def update():
	pass
def delete():
	pass
def search():
	pass
def close():	
	result=messagebox.askyesno('Exit confirmation dialogue box','Are you sure want to close')
	if result==True:
		sys.exit()
	else:
		pass	
def add():
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

#----------------window configuration------------
window=tk.Tk()
window.title("Book Dictionary")
window.geometry('380x350')
window.resizable(width=TRUE,height=TRUE)

#----------------frames configuration----------------
upframe=Frame(window)
upframe.place()

downframe=Frame(window)
downframe.place(x=10,y=50)
##############################-Label and Entries-##########################################################

Label(window,text="Title\t").grid(row=0,column=0)

title_entry=Entry(window)
title_entry.grid(row=0,column=1)
title=title_entry.get()

Label(window,text="Author").grid(row=0,column=3)

author_entry=Entry(window,width=25)
author_entry.grid(row=0,column=4)

Label(window,text="Year\t").grid(row=1,column=0)
year_entry=Entry(window)
year_entry.grid(row=1,column=1)

Label(window,text="ISBN").grid(row=1,column=3)

isbn_entry=Entry(window,width=25)
isbn_entry.grid(row=1,column=4)


# from tkinter import scrolledtext
# main_list=Scrollbar(downframe)
# main_list.grid(row=4,column=1)
# Label(downframe).grid(row=3)
# l=Listbox(downframe,yscrollcommand=main_list.set,width=31,height=16)
# l.grid(row=4,column=0)
#----------------------------------------------
# List all data.
listing = Listbox(downframe,height = 16, width = 35)
listing.grid(row=4,column=3)

# Scrollbar
scroller = Scrollbar(window)
scroller.grid(row=4,column =3)

# Configure scrollbar for Listbox.
listing.configure(yscrollcommand=scroller.set)
scroller.configure(command=listing.yview)

# listing.bind('<<ListboxSelect>>',get_selected_row)
#----------------------------------------------
# main_list.grid(row=4,column=0)
# main_list.insert(INSERT,'Hi !')
# main_list.delete(1.0,END)

#########################= Buttons layout -################################################
o=Label(window)
o.grid(row=3,column=4)

view_all_bt=tk.Button(window,text='View All\t',font=1,width=15,command=view_all,bg="powder blue")
view_all_bt.grid(row=4,column=4)

search_bt=tk.Button(window,text='. Search Entry\t',font=1,width=15,command=search,bg="powder blue")
search_bt.grid(row=5,column=4)

add_bt=tk.Button(window,text='Add Entry\t',font=1,width=15,command=add,bg="powder blue")
add_bt.grid(row=6,column=4)

update_bt=tk.Button(window,text='. Update Selected\t',font=1,width=15,command=update,bg="powder blue")
update_bt.grid(row=7,column=4)

delete_bt=tk.Button(window,text='. Delete Selected\t',font=1,width=15,command=delete,bg="powder blue")
delete_bt.grid(row=8,column=4)
Label(window).grid(row=9)
Label(window).grid(row=10)
close_bt=Button(window,text='Close\t',command=close,font=1,width=15,bg="powder blue")
close_bt.grid(row=11,column=4)
########################################################################yogi6591
window.mainloop()