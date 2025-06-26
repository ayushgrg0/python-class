
import datetime

user_input = "24 August 2005"

date_object = datetime.datetime.strptime(user_input, "%d %B %Y")
print(date_object)

five_years_in_future = date_object + datetime.timedelta(days=5 * 365)

print(five_years_in_future)
