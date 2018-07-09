import pymysql as py

#taking databse username and password
data=open("database_pass.txt","r")
username=data.readline() 
password=data.readline()

#open database connection
db=py.connect("localhost","root",password,"book_dic")

#prepare a cursor object using cursor() method
cursor=db.cursor()

cursor.execute("drop table book")
# cursor.execute("drop table year")
# cursor.execute("drop table ISBN")
# cursor.execute("drop table author")

book="create table book(title char(25),year int,ISBN char(20),author char(20))"
# year="create table book(book_id int,title char(20),char(20),genre char(20))"
# ISBN="create table publishers(publisher_id int,name char(20),street_add char(20),suit_number int,zip_code_id int)"
# author="create table authors(author_id int,first_name char(20),middle_name char(20),last_name char(20))"
print(cursor.execute("show tables"))

cursor.execute(book)
# cursor.execute(year)
# cursor.execute(ISBN)
# cursor.execute(author)

#disconnect from server
db.close()