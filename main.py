from month import month
from year import year

x=input("what do you want to show year or month or exit::")

if "year"==x:
    year.year()
elif "month"==x:
    month.month()
else:
    print("exit")