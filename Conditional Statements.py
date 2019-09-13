# IF is the only conditional statement in pyhton
# if , else statements
# balance = 100
# withdraw =20
# if withdraw <= balance:
#
#     print("withdraw success")
# else:
#     print("insufficient fund")
#
# balance = 100
# withdraw =200
# name = "muyani"
# if withdraw <= balance and name == "said":
#
#     print("withdraw success")
# else:
#     print("insufficient fund or not said")
#
# balance = 100
# withdraw =20
# name = "said"
# if withdraw <= balance and name == "said":
#
#     print("withdraw success")
# else:
#     print("insufficient fund or not said")
#
# # if - elif-else statemet
# score = "excellent"
# if score == "excellent":
#     print("Green lable")
# elif score == "good":
#     print("blue lable")
# elif score == "poor":
#     print("red label")
# else:
#     print("unrecognise")
#
# score = "good"
# if score == "excellent":
#     print("Green lable")
# elif score == "good":
#     print("blue lable")
# elif score == "poor":
#     print("red label")
# else:
#     print("unrecognise")

# ask a user to enter the following marks use input function
# maths
# eng
# kis
# sci
# ssr
# calculate the total marks
# and average and then
# using the average give grade to the student(use an if and elif
# 80 - 100 = "A"
# 70 - <80 = "B"
# 60 - <70 = "C"
# 50 - <60 = "D"

enggrade=input("enter eng grade")
math=input("enter math grade")
kis=input("enter kis grade")
sci=input("enter sci grade")
ssr=input("ssr grade")

total = int(enggrade)+int(math)+int(kis)+int(sci)+int(ssr)
average = int(total)/5
print(average)
if average >= 80 and average<= 100:
    print("A")
elif average >= 70 and average <80:
    print("B")
elif average >= 60 and  average<70:
    print("C")
elif average >=0 and average<50:
    print("F")
else:
    print("not define")



