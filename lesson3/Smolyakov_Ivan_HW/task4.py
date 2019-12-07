import datetime

month = int(input('Enter a month: '))
day = int(input('Enter a day: '))
year = 2019
if month > 12:
    print("error")

now = datetime.datetime(year, month, day)
new_year = datetime.datetime(2020, 1, 1)
delta_days = new_year - now
print('До нового года осталось: ',delta_days)
