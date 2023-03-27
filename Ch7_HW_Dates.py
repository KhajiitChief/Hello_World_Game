import time
import sys
months_list = ["january", "february", "march", "april", "may", "june", "july", "august", "september",
          "october", "november", "december"]
thirty_day_months = [4, 6, 9, 11]
days_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,
             17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]

for i in """Please input a date...
""":
    sys.stdout.write(i)
    sys.stdout.flush()
    time.sleep(.05)



def inputs():
    global month
    month = input("month(typed):").lower()
    global day
    day = int(input("day(number):"))
    global year
    year = int(input("year(number):"))
    print(f"{type(year)}")
def wrong_input():
    for i in """Sorry I did not understand that...
Please enter another date...
""":
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(.05)

    inputs()
def date_month():
    if month in months_list:
        global month_number
        month_number = months_list.index(month) + 1
        return month_number
    else:
        wrong_input()

def date_day():
    if day in days_list:
        if month_number == 2:
            if day > 28:
                wrong_input()
            else:
                return day
        elif month_number in thirty_day_months:
            if day > 30:
                wrong_input()
            else:
                return day
        else:
            return day
    else:
        wrong_input()

def date_year():
    if year >= 0:
        return year
    else:
        wrong_input()
inputs()

def rturn():
    print(date_month(), "/", date_day(), "/", date_year())
rturn()