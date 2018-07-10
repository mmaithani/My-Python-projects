import pymysql as py
# from frontend import *
#----------Taking databse username and password-------------
data=open("database_pass.txt","r")
username=data.readline() 
password=data.readline()

#----------open database connection---------------------------
db=py.connect("localhost","root",password,"book_dic")

#--------prepare a cursor object using cursor() method----------
cursor=db.cursor()

#########################- Button commands -################################################

