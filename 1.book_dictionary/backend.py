import pymysql as py
from tkinter import *
import sqlite3
# from frontend import *
#----------Taking databse username and password-------------
data=open("database_pass.txt","r")
username=data.readline() 
password=data.readline()

#---------------open database connection---------------------db = conn_obj
db=py.connect("localhost","root",password,"book_dic")      #cursor_obj=cursor

#--------prepare a cursor object using cursor() method----------
cursor=db.cursor()
	
#########################- Button commands -################################################
def view_alll():
	db=sqlite3.connect("book_dic.db")
	cursor=db.cursor()
	cursor.execute("select * from book")
	row=cursor.fetchall()
	db.close()
	return row
	

# def add():
# 	cursor.execute("insert into book (title,year,ISBN,author)values( 'title_entry.get()','year_entry.get()','isbn_entry.get()','author_entry.get()')
# 	db.commit()
# 	cursor.execute("insert into book(title,year,ISBN,author)values('dfj','65','5','eee')")
