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
        "CREATE TABLE IF NOT EXISTS sensor_data (time TIMESTAMP PRIMARY KEY, temp FLOAT, pressure FLOAT, altitude FLOAT)")
    db.commit()


# setup
sensor = BMP180.BMP085(busnum=1)

database_setup()
# read and save data
while True:
    #time_now = int(time.time())
    time_now = datetime.time(time.ctime())
    print(time_now)
    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude()

    cursor.execute("INSERT INTO sensor_data (time, temp, pressure, altitude) VALUES "
                   "(%s, %s, %s, %s)", (time_now, temp, pressure, altitude))

    db.commit()
    print(f"Data saved at {time_now}")
    time.sleep(0.5)

