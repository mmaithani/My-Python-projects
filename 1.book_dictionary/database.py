import pymysql as py

#taking databse username and password
data=open("database_pass.txt","r")
username=data.readline() 
password=data.readline()

#open database connection
db=py.connect("localhost","root",password,"book_dic")

#prepare a cursor object using cursor() method
cursor=db.cursor()

#execur=ting uerry using execute() method
cursor.execute("SELECT VERSION()")

#fetch single row uing fetchone method()
deta=cursor.fetchone()
print("Database version : %s"% deta)

book="create table book(book_id int,title char(20),location char(20),genre char(20))"
title="create table titles(title_id int,title char(20),ISBN char(20),publisher_id int,publication_year int)"
ISBN="create table publishers(publisher_id int,name char(20),street_add char(20),suit_number int,zip_code_id int)"
zip_code="create table zip_code(zip_code_id int,city char(20),state char(20),zip_code int)"
auther_titles="create table auther_titles(auther_title_id int,aurther_id int,title_id int)"
authors="create table authors(author_id int,first_name char(20),middle_name char(20),last_name char(20))"

cursor=db.cursor()

cursor.execute("drop table book")
cursor.execute("drop table titles")
cursor.execute("drop table publishers")
cursor.execute("drop table zip_code")
cursor.execute("drop table auther_titles")
cursor.execute("drop table authors")

print(cursor.execute("show tables"))

cursor.execute(book)
cursor.execute(titles)
cursor.execute(publishers)
cursor.execute(zip_code)
cursor.execute(auther_titles)
cursor.execute(authors)

print(cursor.execute("show tables"))

#disconnect from server
db.close()