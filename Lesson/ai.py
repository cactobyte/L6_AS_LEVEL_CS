import random
# Store
c = int(input("Memory Efficiency Number>>"))
#       M     L    R
mem = [c/2, c/2, c/2]
def decisionPoint(meLimit, leftJ, rightJ, mem):
    r = random.randint(0, 6)
    if r > meLimit: #numba bigga than go right and put in route path vice verca
        route.append(rightJ) #Pick RIght
        print("Number simulated: ", r)

    else:
        route.append(leftJ)
        print(r, "Left")

exitPoint = random.randint(4, 7)

while True:
    route = []
    # Decision Point One - Mid
    decisionPoint(mem[0], 2, 3) #Odds of 3, pick between 2,3
    if route[0] == 3: #2nd Decision Point
        decisionPoint(mem[2], 6, 7)
    else:
        decisionPoint(mem[1], 4, 5)
    if route[1] == exitPoint:
        print("Route Found")
    else:
        print("", route, exitPoint) #Route was wrong, updating mems



    input("Enter to Simulate\n")
