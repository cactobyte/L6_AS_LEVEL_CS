weight = [1500, 2000, 3000, 4000]
x = 0
for i in weight:
    x += i

average = x / len(weight)
print("The average is: ", average)

y = 0
z = 1
for i in weight:
    if i < average-500:
        y += i
        z += 1

lowAverage = y / z
print("The low average is: ", lowAverage)


### q3

mark = [[4, 0], [3, 1], [3, 2], [5, 3], [1, 4]]

for x in range(0, 5):
    studentMark = int(input("Please enter the score that student {} achieved".format(x+1)))
    mark.append([studentMark, x])

### q4
