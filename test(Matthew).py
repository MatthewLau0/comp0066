import datetime

refugee_dob = input("Please enter the refugee date of birth (yyyy/mm/dd format): ")


today = datetime.date.today()
x = refugee_dob.split("/")
birthyear = int(x[0])
birthmonth = int(x[1])
birthday = int(x[2])

birthdate = datetime.date(birthyear, birthmonth, birthday)
age = 0

if birthdate.month < today.month and today.year > birthdate.year:
    age = today.year - birthdate.year

elif birthdate.month > today.month and today.year > birthdate.year:
    age = today.year - birthdate.year - 1

elif birthdate.month == today.month and today.year > birthdate.year and today.day < birthdate.day:
    age = today.year - birthdate.year - 1

elif birthdate.month == today.month and today.year > birthdate.year and today.day > birthdate.day:
    age = today.year - birthdate.year

print(age)