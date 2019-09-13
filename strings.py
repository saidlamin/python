# # strings are enclosed in speech marks
# # this is to tell python that take that value literally
# # string are also called literally
# name = "Said Lamin + me"
# marks = "23+42+60+64"
phone_number = "70345567"
print(type(phone_number))
#
#
# # typecasting
# phone_number = int(phone_number)
# print(phone_number)
# print(type(phone_number))
# phone_number = str(phone_number)
#
#
#
# # print(name)
# # print(marks)
# # print(type(phone_number))
#


# String operations
first_name = "said"
second_name = "Najib"


# we use a plus operator to concat strings
full_name = first_name + second_name
full_name = first_name + " " + second_name
print(full_name)
print(full_name)

print(first_name.title())
print(first_name.upper())
print(first_name.lower())
print(full_name.split())
print(full_name.count("a"))

gender = "mmmffmmfmfmfffmfmfffffmfmf"
print(gender.count("f"))
print(gender.count("m"))