'''
Datenbank Übung
Phillip Hilscher
'''

import mysql.connector as mariadb

mydb = None
mycursor = None

def database_setup():
    global mydb
    mydb = mariadb.connect(host="localhost",user="phil",password="phil")

    global mycursor

    mycursor = mydb.cursor()

    mycursor.execute("USE python_test_01")


database_setup()


while(True):
    name = input("Please input your name, 'end' closes the program and displays the whole database")
    
    if (name == "end"):
        break
    
    number_list = []
    
    print("Input a number or 'end' to finish")
    while(True):
        number = input("number ->")
        if (number == "end"):
            break
        else:
            number = int(number)
            number_list.append(number)


    number = len(number_list)
    summe = sum(number_list)
    
    


    sql = "INSERT IGNORE INTO werte (name,number,sum) VALUES (%s,%s,%s)"

    daten = (name, number, summe)

    
    mycursor.execute(sql, daten)
    mydb.commit()



print("Values in the table:")
mycursor.execute("SELECT * FROM werte")
for x in mycursor:
        print(x)


