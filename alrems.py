from datetime import datetime
setAlarm = input("Set alarm time in 24-hour format (HHMM): ")

while True:
      now=datetime.now().strftime("%H:%M")

      if  now == setAlarm:
         print("Hello")
         break

