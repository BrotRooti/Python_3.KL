# imports
import datetime

import Adafruit_BMP.BMP085 as BMP180
import mysql.connector as mariadb
import time

db = None
cursor = None


def database_setup():
    global db
    db = mariadb.connect(host="localhost", user='phil', password='phil')

    global cursor

    cursor = db.cursor()

    cursor.execute("USE sensor")
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS sensor_data (id int AUTO_INCREMENT PRIMARY KEY, temp FLOAT, pressure FLOAT, altitude FLOAT, "
        "time DATETIME)")
    db.commit()


# setup
sensor = BMP180.BMP085(busnum=1)

database_setup()
# read and save data
while True:
    #time_now = int(time.time())
    time_now = time.ctime()
    print(time_now)
    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude()

    cursor.execute("INSERT INTO sensor_data (temp, pressure, altitude, time) VALUES "
                   "(%s, %s, %s, current_timestamp)", (temp, pressure, altitude))

    db.commit()
    print(f"Data saved at {time_now}")
    time.sleep(1)

