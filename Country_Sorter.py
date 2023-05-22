'''
Problem: I need to open the text file(which cantains country names) and uppercase all the letters. Then I have to alphabetize them.
Q1 : Print all the countries in the file.
Q2 : Print all the countries in ascending order.
Q3 : Print all the countries in descending order.
Q4 : List all the countries that starts with a given letter by user.
Q5 : List all the countries that have these given letters by user.
Q6 : List all the countries with a given length.
'''

c = open("Countries.txt", "r")
print(type(c))
str_countries = c.read()
#1. print countries
print(str_countries)
#2 capitalise
print(str_countries.upper())
# Ascending order

arr_countries = str_countries.split("\n")
print(arr_countries)