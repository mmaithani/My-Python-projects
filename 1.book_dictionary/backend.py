import pymysql as py

#----------Taking databse username and password-------------
data=open("database_pass.txt","r")
username=data.readline() 
password=data.readline()

#----------open database connection---------------------------
db=py.connect("localhost","root",password,"book_dic")

#--------prepare a cursor object using cursor() method----------
cursor=db.cursor()

#########################- Button commands -################################################

def view_all():
	cursor.execute("select * from book")
	result=cursor.fetchall()
def search():	
	pass
def add():
	pass
def update():
	pass
def delete():
	pass

add

#disconnect from server
db.close()