import tkinter as tk  #assigning tkinter a small name-tk for writeability
from tkinter import *
from tkinter import scrolledtext
from tkinter import messagebox
import sys
import backend
def add_command():
    """Insert entry via button."""
    backend.insert(title_text.get(),
                    author_text.get(),
                    year_text.get(), 
                    isbn_text.get())
    listing.delete(0, END)
    listing.insert(END, 
                    (title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get()))

def view_commmand():
    """View entries via button."""
    listing.delete(0, END)
    for row in backend.view():
        listing.insert(END, row)

def update_command():
    """Update entry via button."""
    backend.update(selected_tuple[0], 
                    title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get())

def delete_command():
    """Delete entry via button."""
    backend.delete(selected_tuple[0])

def search_command():
    """Search entry via button."""
    listing.delete(0, END)
    for row in backend.search(title_text.get(), 
                                author_text.get(), 
                                year_text.get(), 
                                isbn_text.get()):
        listing.insert(END, row)

def get_selected_row(event):
    """Pre-fill fields for selected entry."""
    global selected_tuple
    index = listing.curselection()[0]
    selected_tuple = listing.get(index)

    entry1.delete(0, END)
    entry1.insert(END, selected_tuple[1])

    entry2.delete(0, END)
    entry2.insert(END, selected_tuple[2])

    entry3.delete(0, END)
    entry3.insert(END, selected_tuple[3])

    entry4.delete(0, END)
    entry4.insert(END, selected_tuple[4])
#---------------------------------------------------------------------
# def view_all():
# 	# for row in backend.view_alll():
# 	# main_list.grid(row=4,column=0)
# 		# main_list.insert(1,'row')
# 	# main_list.delete(1.0,END)
# 	import backend
# 	listing.delete(0,END)
# 	for row in backend.view_alll():
# 		listing.insert(END,row)

# def update():
# 	pass
# def delete():
# 	pass
# def search():
# 	pass
def close():	
	result=messagebox.askyesno('Exit confirmation dialogue box','Are you sure want to close')
	if result==True:
		sys.exit()
	else:
		pass	
# def add():
	# pass 
########################################################################################################	
# 
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

title_text=Entry(window)
title_text.grid(row=0,column=1)

Label(window,text="Author").grid(row=0,column=3)

author_text=Entry(window,width=25)
author_text.grid(row=0,column=4)

Label(window,text="Year\t").grid(row=1,column=0)
year_text=Entry(window)
year_text.grid(row=1,column=1)

Label(window,text="ISBN").grid(row=1,column=3)

isbn_text=Entry(window,width=25)
isbn_text.grid(row=1,column=4)


listing = Listbox(downframe,height = 16, width = 35)
listing.grid(row=4,column=3)

# Scrollbar
scroller = Scrollbar(window)
scroller.grid(row=4,column =3)

# Configure scrollbar for Listbox.
listing.configure(yscrollcommand=scroller.set)
scroller.configure(command=listing.yview)

# listing.bind('<<ListboxSelect>>',get_selected_row)

#########################= Buttons layout -################################################
o=Label(window)
o.grid(row=3,column=4)

view_all_bt=tk.Button(window,text='View All\t',font=1,width=15,command=view_commmand,bg="powder blue")
view_all_bt.grid(row=4,column=4)

search_bt=tk.Button(window,text='. Search Entry\t',font=1,width=15,command=search_command,bg="powder blue")
search_bt.grid(row=5,column=4)

add_bt=tk.Button(window,text='Add Entry\t',font=1,width=15,command=add_command,bg="powder blue")
add_bt.grid(row=6,column=4)

update_bt=tk.Button(window,text='. Update Selected\t',font=1,width=15,command=update_command,bg="powder blue")
update_bt.grid(row=7,column=4)

delete_bt=tk.Button(window,text='. Delete Selected\t',font=1,width=15,command=delete_command,bg="powder blue")
delete_bt.grid(row=8,column=4)
Label(window).grid(row=9)
Label(window).grid(row=10)
close_bt=Button(window,text='Close\t',command=close,font=1,width=15,bg="powder blue")
close_bt.grid(row=11,column=4)
########################################################################yogi6591
window.mainloop()