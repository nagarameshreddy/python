import datetime
print(datetime.date.today())
print(datetime.datetime.now())

today = datetime.date.today()
text = '{today.month}/{today.day}/{today.year}'.format(today=today)
print(text)
text1= '{today.day}-{today.month}-{today.year}'.format(today=today)
print(text1)
print("Month,day and year")
print(today.month)
print(today.day)
print(today.year)