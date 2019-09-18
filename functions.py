# a function is a named reusable blocked of code use to perform a related action
a = 0
b = 0

a = a + 2
b = a + 3
# def is the keyword to create a new function
# add_two_numbers is the name of for our function
# a and b are called parameters of a function
# c is the return value
# definig a function
def add_two_numbers(a,b):
    c = a+b
    return c

def add_two_names(firstname,lastname):
    full_name = firstname+lastname
    return full_name
res = add_two_numbers("Said","Lamin")
# print(res)

# application
student1 = [12,23,34,45,65]
student2 = [22,23,34,45,65]
student3 = [32,23,34,45,65]
student4 = [42,23,34,45,65]

def find_total(math,eng,kis,ssr,sci):
#    alama below is locally scoped inside the function
    total = math+eng+kis+ssr+sci
    return alama
def find_average(tot):
    return tot/5
# marks = find_average(12,23,34,45,65)
# ave = find_average(marks)


total1 = student1[0] + student1[1] + student1[2] + student1[3] + student1[4]
total2 = student2[0] + student2[1] + student2[2] + student2[3] + student2[4]
total3 = student3[0] + student3[1] + student3[2] + student3[3] + student3[4]
total4 = student4[0] + student4[1] + student4[2] + student4[3] + student4[4]
def find_average():
    pass

average1 = total1/5
average2 = total2/5
average3 = total3/5
average4 = total4/5

# write the function called sum_digit that give an integer num and return the sum of the digit of num

# def sum_digits(num):
#     sum_of_digit = 0
#     num= str(num)
#     for i in num:
#         sum_of_digit = sum_of_digit + int(i)
#     return sum_of_digit
# res= sum_digits(1234)
# print(res)


