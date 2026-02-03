#!/usr/bin/python3

# contains a sample program that asks you for a year, a month and a day.

# month list
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

# endings list
endings = ["st", "nd", "rd"] + 17 * ["th"] \
        + ["st", "nd", "rd"] + 7 * ["th"] \
        + ["st"]


# inputs
year = input("Year: ")
month = input("Month: ")
day = input("Day: ")

month_name = months[int(month) - 1]
day_number = day + endings[int(day) - 1]

print(month_name + " " + day_number + ", " + year)
