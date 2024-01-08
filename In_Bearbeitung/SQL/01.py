import mysql.connector as mariadb
#
def database_setup():
	mydb = mariadb.connect(host="localhost",user='phil',password='phil')

	myc = mydb.cursor()
	myc.execute("SHOW DATABASES")
	for x in myc:
        	print(x)



#first call the setup functiom
database_setup()
