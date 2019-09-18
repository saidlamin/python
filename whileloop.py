# a whileloop repeats until a specified condition is false
a = 1
# the conbdition we are taking about is "a<10"
# while a < 11:
#    print (a)
 #   a = a+1

#while a < 11:
#    print ("Said "*a)
#    a = a+1
#while a <101:
#   print(a)
#    a=a+2
#while a <=100:
#    print(a)
#    a = a+2
# savepin = "0000"
# enterpin = input("enterpin")
# while savepin != enterpin:
#     enterpin = input("enterpin")
#
# print("successful")
savedpin = "0000"
trails = 3

enteredpin = input("enterpin")
trails = trails-1
while savedpin != enteredpin and trials > 0:
    enteredpin = input("enterpin")
    trials = trials-1
else:
        if trials < 1 and enteredpin != savedpin:
            print("card swallowed")
        else:
            print("successful")

