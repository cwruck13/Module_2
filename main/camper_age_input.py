"""
Program: camper_age_input.py
Author: Cassandra Wruck
Last date modified: June 1st, 2020

The program will have will prompt for the age of one infant (age 1-5 years)
who is attending camp and convert the age in months to years via a function call then print the result.
"""

# get input from user
years = input('What is your age?: ')


# method to convert years to months
def convert_to_months(years):
    years_int = int(years)
    months = years_int * 12
    return months


# printing return
if __name__ == '__main__':
    print(str(convert_to_months(years)) + ' months')
