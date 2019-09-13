tasklist =[23,
           "jane",
           ["lesson 23",560,{"currency":"kes"}],
           987,
           (76,"john")]
# 1. determing the type of variable in tasklist using an inbuild function- roy
print
# 2. print  kes- said
# 3 print 560 - patricia
# 4 use a function to determine the lenth of tasklist
# 5. change 987 to 789 using indexing only najib
# 6 change the name "john" to jane - alex

print(type (tasklist))
print(tasklist)
print(tasklist[2][2]["currency"])
print(len(tasklist))
a = tasklist[3] = "789"
print(a)
b = tasklist[3]

print(b)
