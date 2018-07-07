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

cursor.execute("create database book_dic")
name=fetchone()
print("%s"%name)
#disconnect from server
db.close()