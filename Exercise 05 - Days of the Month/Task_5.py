months={
    "January":"31",
    "Feburary":"28",
    "March":"31",
    "April":"30",
    "May":"31",
    "June ":"30",
    "July":"31",
    "August":"31",
    "September":"30",
    "October":"31",
    "November":"30",
     "Dcember":"31"
}
# Dictionary of months and number of days
months = {
    1: 31,
    2: 28,  # will change for leap year
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}

month = int(input("Enter month number (1-12): "))

if month in months:
    if month == 2:
        leap = input("Is it a leap year? (yes/no): ")
        if leap == "yes":
            print("February has 29 days.")
        else:
            print("February has 28 days.")
    else:
        print("This month has", months[month], "days.")
else:
    print("Invalid month number.")