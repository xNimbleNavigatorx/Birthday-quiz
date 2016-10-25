"""
birthday.py
Author: xNimbleNavigatorx
Credit: l
Assignment:

Your program will ask the user the following questions, in this order:

1. Their name.
2. The name of the month they were born in (e.g. "September").
3. The year they were born in (e.g. "1962").
4. The day they were born on (e.g. "11").

If the user's birthday fell on October 31, then respond with:

  You were born on Halloween!

If the user's birthday fell on today's date, then respond with:

  Happy birthday!

Otherwise respond with a statement like this:

  Peter, you are a winter baby of the nineties.

Example Session

  Hello, what is your name? Eric
  Hi Eric, what was the name of the month you were born in? September
  And what year were you born in, Eric? 1972
  And the day? 11
  Eric, you are a fall baby of the stone age.
"""
from datetime import datetime
from calendar import month_name
todaymonth = datetime.today().month
todaydate = datetime.today().day

name = input("Hello, what is your name? ") 
month = input("Hi " + name + ", what was the name of the month you were born in? ")
year = int(input("And what year were you born in, " + name + "? "))
day = input("And the day? ")

if month == "December" or "January" or "February":
    season = "winter"
if month == "March" or "April" or "May":
    season = "spring"
if month == "June" or "July" or "August":
    season = "summer"
if month == "September" or "October" or "November":
    season = "fall"
    
if year >= 2000:
    age= "two thousands"
if year >= 1990 and year < 2000:
    age= "nineties"
if year >= 1980 and year < 1990:
    age= "eighties"
if year < 1980:
    age= "Stone Age"

if todaymonth == 1:
    todaymonth == "January"
elif todaymonth == 2:
    todaymonth = "February"
elif todaymonth == 3:
    todaymonth = "March"
elif todaymonth == 4:
    todaymonth = "April"
elif todaymonth == 5:
    todaymonth = "May"
elif todaymonth == 6:
    todaymonth = "June"
elif todaymonth == 7:
    todaymonth = "July"
elif todaymonth == 8:
    todaymonth = "August"
elif todaymonth == 9:
    todaymonth = "September"
elif todaymonth == 10:
    todaymonth = "October"
elif todaymonth == 11: 
    todaymonth = "Novemember"
elif todaymonth == 12:
    todaymonth = "December"

if month == "October" and day == "31":
    print("You were born on Halloween!")
elif month == todaymonth and int(day) == todaydate:
    print("Happy Birthday!")
else:
    print(name + ", you are a " + season + " baby of the " + age + ".")
