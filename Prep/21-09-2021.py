n = int(input())

if n < 2:
    print(1)
else:
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    print(fact)
#
# import math
# print(math.factorial(n))

#### FACTORIAL


