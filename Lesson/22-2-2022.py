TWO TWO TWO TWO TWO


def SortMyArray(array):
    n = int(len(array))
    swapped, temp = False, 0


    while swapped == False:
        for i in range(0, n-1):
            if array[i] <= array[i + 1]:
                temp = array[i + 1]
                array[i] = temp
                swapped = True
    return array

poop = [1, 5, 2, 6, 10]
n = SortMyArray(poop)

print(n)
print(poop)

doesnt work
