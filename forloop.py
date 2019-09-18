
from functions import add_two_numbers

# for a in range(10,101):
#     print(a)
# fruits = ["mango","apple","pears","banana","avocado","guava","berry"]
#
# for fruit in fruits:
#     print(fruit)
# fruits = ["mango","apple","pears","banana","avocado","guava","berry"]
#
# for each in fruits:
#     each= each + "a"
#     print(each)
# find the sum of numbers from 0-9
# sum = 0
# for each in range(10):
#     sum = each+ sum
# print(sum)

# name= ("said")
# for each in range(10):
#
#     print(name)

# name= ("said")
# for each in range (100):
#
#     print(each,"name")
# a =0
# for each in range(8,90,3):
#
#     print(each)

first_name = eval(input("enter first number"))
second_number =eval(input("enter second number"))
result = add_two_numbers(first_name,second_number)
print(result)