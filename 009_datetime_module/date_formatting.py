
import datetime

# nested module
ayush_dob = datetime.datetime(2005, 8, 24)

# formatting the date in year, month and day
formatting_date = ayush_dob.strftime("%Y %B %a")

print(formatting_date)
