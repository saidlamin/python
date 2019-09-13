personal = ["said lamin", "0700", "26","nairobi"]


# this ia an interger
a = 0
# this is string
b = ""
# list
c = []
# tuple
d = ()
# dic
e = {}

dic = {"name":"said","phone_number":"0700","age":"26","location":"nairobi","marks":{"maths":32,"hausa":27,"sci":38},
"date_of_birth":(24,"dec",1990)}
print(type(dic))


print(dic["phone_number"])
print(dic["age"])
print(len(dic))
print(dic["marks"])
print(dic["marks"]["maths"])
print(dic["date_of_birth"])
print(type(dic["date_of_birth"]))
print(dic["location"])
print(dic)