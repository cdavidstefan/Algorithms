# input --> birth year
# output --> age

from datetime import date

birth_year = int(input("Enter your birth year: "))
birth_month = int(input("Enter your birth month: "))
birth_day = int(input("Enter your birth day: "))


def calculate_age(birth_year, birth_month):
    if birth_month >= date.today().month and birth_day > date.today().day:
        age = date.today().year - birth_year - 1
    else:
        age = date.today().year - birth_year
    print(f"You are {age} years old.")


print(calculate_age(birth_year, birth_month))
