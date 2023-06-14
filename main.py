
import time 
from datetime import datetime

def getTimestamp():
    return int(time.time())

specific = datetime(2023, 6, 13, 20, 15, 0)
specific = int(time.mktime(specific.timetuple()))

def addminutestoTimestamp(timestamp, minutes):
    return timestamp + (minutes * 60)

def TimestampToDatetime(timestamp):
    return datetime.fromtimestamp(timestamp)

def countdown(start, end):
    while start < end:
        print(datetime.fromtimestamp((end - start)))
        start += 1
        time.sleep(1)



while True:
    t= getTimestamp()
    specific = addminutestoTimestamp(specific, 135)
    if t < specific:
        print("helltide is coming in")
        countdown(t, specific)

    