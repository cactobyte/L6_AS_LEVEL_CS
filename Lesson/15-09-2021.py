user = int(input())
if 2 <= user <= 12:
    n = 1
    while n < 13:
        print("{} x {} = {}".format(user, n, user*n))
        n += 1
else:
    print("Number too large or too small")
    
# # # # # # # # # # # # # #
 
import random

r = random.randint(1, 25)
correct = False
while correct != True:
    ans = r*r
    answer = int(input("What is the square of {}".format(r)))
    if(answer == ans):
        correct = True
        print("Your correct")
    else:
        print("Your wrong dumbass")
