number = int(input())
root = 1
while (root * root) < number:
    root += 1
d = 2
FactorFound = False
while (FactorFound == False) and (d <= root): # not(FactorFound)
    r = number % d
    if(r == 0):
        FactorFound = True
    d += 1

if FactorFound == False:
    print("Prime")
else:
    print("Not Prime")

#### finding prime numbers

lyrics = ["and a partridge in a pear tree.", "Two turtle doves", "Three French hens,", "Four calling birds,", "Five golden rings,", "Six geese a-laying,", "Seven swans a-swimming,", "Eight maids a-milking,", "Nine ladies dancing,", "Ten lords a-leaping,", "Eleven pipers piping,", "Twelve drummers drumming,"]
dayName = ["first", "second", "third", "forth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth", "eleventh", "twelfth"]
days = 12
for day in range(1, 13):
    print("\nOn the {} of Christmas my truelove sent to me,".format(dayName[day-1]))
    for i in range(day+1, 1, -1):
        if(day < 2):
            print("a partridge in a pear tree")
        else:
            print(lyrics[i-2])

