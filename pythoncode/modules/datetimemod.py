from datetime import  UTC, datetime,timezone
import os
timenow = datetime.now()    # datetime.datetime.now()  # get the current date and time
print(timenow)
print(timenow.year)  # get the year
print(timenow.month)  # get the month
print(timenow.day)  # get the day
print(timenow.hour)  # get the hour

timezonedata = datetime.now(timezone.utc)  # get the current date and time in UTC timezone
print(timezonedata)

custom_date = datetime.strftime(timenow, "%d_%m_%Y")  # format the date and time in a custom format
create_file = os.system(f"touch app.log_{custom_date}.txt")  # create a file with the custom date format as the name
