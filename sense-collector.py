from sense_hat import SenseHat
from pymongo import MongoClient
import time
from datetime import datetime

#sensehat
sense = SenseHat()

#mongo 
client = MongoClient('mongodb://192.168.0.100:49157/')
db = client.senzori
collection = db.inputs

try: db.command("serverStatus")
except Exception as e: print(e)
else: print("You are connected!")

def insert(document):
    try:
        collection.insert_one(document)
        # print(document)
        return True
    except Exception as e:
        print("An exception ::", e)
        return False

def main():
    payload = {
        "Date" : datetime.today().replace(microsecond=0),
        "Temp" : sense.get_temperature(),
        "TempFromHumidity": sense.get_temperature_from_humidity(),
        "TempFromPresure" : sense.get_temperature_from_pressure(),
        "Presure": sense.get_pressure(),
        "Humidity": sense.get_humidity(),
        "Orientation": sense.get_orientation(),
        "Accelerometer": sense.get_accelerometer_raw(),
    }
    print(insert(payload))

while True:
    main()
    time.sleep(10)
