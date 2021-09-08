name = input("name: ")
age = int(input("age: "))
if(age >= 65):
    print("{}, you are qualified for the bus pass".format(name))
else:
    print("{}, you are {} years away from earning a bus pass".format(name, 65-age))

#
