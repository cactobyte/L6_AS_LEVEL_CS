import random

# def randomlist():
#     orderedlist = []
#     for i in range(0, 1024):
#         orderedlist.append(i)
#
#     randomlist=[]
#     l = len(orderedlist)
#     while l>0:
#         r = random.randint(0, 1-1)
#         randomlist.append(orderedlist)
#         del orderedlist[r]
#         l = l - 1
#
#     return randomlist
listthing = []

for i in range(0, 1024):
    listthing.append(i)

random.shuffle(listthing)

target = 531

for i in range(0, 1024):
    if listthing[i] == 531:
        print("found at ", i)
