import datetime

# displaying only the date

ayush_dob = datetime.date(2005, 8, 24)

five_years_before = ayush_dob - datetime.timedelta(days=3 * 365)

print(f'Date of birth with date only ----> {five_years_before}')

print('=' * 70)

# displaying the date and time both

ayush_dob_with_time = datetime.datetime(2005, 8, 24, 0, 0, 0)

five_years_before_time = ayush_dob_with_time + datetime.timedelta(hours=3, minutes=24, seconds=25)

print(f'Date of birth with date and time both  -----> {five_years_before_time}')


# days

# hours
# minutes
# seconds
# microseconds
