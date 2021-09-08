name = input("name: ")
age = int(input("age: "))
if(age >= 65):
    print("{}, you are qualified for the bus pass".format(name))
else:
    print("{}, you are {} years away from earning a bus pass".format(name, 65-age))

#

amount = int(input())
if(amount<500):
    rate = 0.01
elif(amount < 3000):
    rate = 0.015
elif(amount < 10000):
    rate = 0.02
else:
    rate = 0.035

print(rate)

