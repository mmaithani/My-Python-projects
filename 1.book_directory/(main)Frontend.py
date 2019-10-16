from tkinter import *
import backend
import os
from PIL import ImageTk,Image
from tkinter import messagebox
#window configuration
window = Tk()
window.geometry("500x500")
window.wm_title("Book Directory")
window.configure(background="",bg="#a1dbcd")
window.wm_iconbitmap('icon.ico')

global selected_tuple

def add_command():
    """Insert entry via button."""
    backend.insert(title_text.get(),
                    author_text.get(),
                    year_text.get(), 
                    isbn_text.get())
    
    # listing.delete(0, END)
    listing.insert(END, 
                    (title_text.get(),
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get()))
                
def view_command():
    """View entries via button."""
    listing.delete(0, END)
    for row in backend.view():
        listing.insert(END, row)

def update_command():
    """Update entry via button."""
    # global selected_tuple
    backend.update(selected_tuple[0], 
                    title_text.get(), 
                    author_text.get(), 
                    year_text.get(), 
                    isbn_text.get())

def delete_command():
    """Delete entry via button."""
    global selected_tuple
    backend.delete(selected_tuple[0])

def search_command():
    """Search entry via button."""
    listing.delete(0, END)
    for row in backend.search(title_text.get(), 
                                author_text.get(), 
                                year_text.get(), 
                                isbn_text.get()):
        listing.insert(END, row)
def close():
    result=messagebox.askyesno('Exit confirmation','Are you want to Exit')
    if result==True:
        sys.exit()
    else:
        pass
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



# Labels for entry fields.
label1 = Label(window, text = "Title",fg="#383a39",bg="#a1dbcd",font=("Helvetica",16))
label1.place(x=400,y=0)
label2 = Label(window, text = "Author",fg="#383a39",bg="#a1dbcd",font=("Helvetica",16))
label2.place(x=400,y=50)

label3 = Label(window, text = "Year",fg="#383a39",bg="#a1dbcd",font=("Helvetica",16))
label3.place(x=400,y=95)

label4 = Label(window, text = "ISBN",fg="#383a39",bg="#a1dbcd",font=("Helvetica",16))
label4.place(x=400,y=140)

# Entry Fields.
title_text = StringVar()
entry1 = Entry(window, textvariable = title_text)
entry1.place(x=370,y=30)

author_text = StringVar()
entry2 = Entry(window, textvariable = author_text)
entry2.place(x=370,y=75)

year_text = StringVar()
entry3 = Entry(window, textvariable = year_text)
entry3.place(x=370,y=120)

isbn_text = StringVar()
entry4 = Entry(window, textvariable = isbn_text)
entry4.place(x=370,y=175)


# List all data.
listing = Listbox(window, height = 16, width = 59)
listing.grid(row=1,column=0)

listing.bind('<<ListboxSelect>>', get_selected_row)
# Scrollbar.
scroller = Scrollbar(window)
scroller.place(x=340,y=103,height=257)
# Configure scrollbar for Listbox.
listing.configure(yscrollcommand = scroller.set)
scroller.configure(command = listing.yview)

listing.bind('<<ListboxSelect>>', get_selected_row)
# Buttons for various operations on data.
button1 = Button(window, 
                text = "View All", 
                width = 12, 
                command = view_command,fg="#a1dbcd",bg="#383a39")
button1.place(x=370,y=200)

button2 = Button(window, 
                text = "Search Entry", 
                width = 12, 
                command = search_command,fg="#a1dbcd",bg="#383a39")
button2.place(x=370,y=225)

button3 = Button(window, 
                text = "Add Entry", 
                width = 12, 
                command = add_command,fg="#a1dbcd",bg="#383a39")
button3.place(x=370,y=250)

button4=Button(window,
                text="Update", 
                width = 12, 
                command = update_command,fg="#a1dbcd",bg="#383a39")
button4.place(x=370,y=275)

button5 = Button(window, 
                text = "Delete Selected", 
                width = 12, 
                command = delete_command,fg="#a1dbcd",bg="#383a39")
button5.place(x=370,y=300)

button6 = Button(window, 
                text = "Close", 
                width = 12, 
                command = close,fg="#a1dbcd",bg="#383a39")
button6.place(x=370,y=325)

import webbrowser

def callback(event):
    webbrowser.open_new("https://github.com/mmaithani")
def callback2(event):
    webbrowser.open_new("https://github.com/mmaithani/My-Python-projects/tree/master/1.book_dictionary")
def insta(event):
    webbrowser.open_new("https://www.instagram.com/aee_nobody/")
def twitter(event):
    webbrowser.open_new("https://twitter.com/e9a16bb235e6485?lang=en")
# root= Tk()
#---------------------------------------------------------------------------------------------
img = ImageTk.PhotoImage(Image.open("banner.gif"))
panel = Label(window, image = img)
panel.grid(row=0,column=0)
###############################################################################################
link = Label(window, text="Github profile",fg='blue',bg="#a1dbcd", cursor="hand2")
link.place(x=0,y=412)
link.bind("<Button-1>", callback)

link2 = Label(window, text="Github project link", fg="blue",bg="#a1dbcd", cursor="hand2")
link2.place(x=0,y=430)
link2.bind("<Button-1>", callback2)

profile = ImageTk.PhotoImage(Image.open("github_profile_pic.png"))
panel = Label(window, image =profile)
panel.place(x=10,y=360)
#---------------------------------------------------------------------------------------
instagram= ImageTk.PhotoImage(Image.open("insta.png"))
panel = Label(window, image =instagram)
panel.place(x=110,y=365)

link2 = Label(window, text="Instagram", fg="blue",bg="#a1dbcd", cursor="hand2")
link2.place(x=110,y=410)
link2.bind("<Button-1>", insta)
#--------------------------------------------------------------------------------------------------

tweet= ImageTk.PhotoImage(Image.open("twitter.png"))
panel = Label(window, image =tweet)
panel.place(x=180,y=362)

link2 = Label(window, text="Twitter", fg="blue",bg="#a1dbcd", cursor="hand2")
link2.place(x=180,y=410)
link2.bind("<Button-1>", twitter)
#--------------------------------




# Keep window open until closed.
window.mainloop()
