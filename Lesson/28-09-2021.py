def factorial(n):
    if n == 0:
        return 1
    else:
        f = 1
        for i in range(2, n+1):
            f *= i
    return f

print(factorial(2))
print(factorial(3))
print(factorial(4))
# 
# import math
# print(math.factorial(2),math.factorial(3),math.factorial(4))
#oof
