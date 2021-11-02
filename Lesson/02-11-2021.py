 def BinaryToInt(binthing):  # Requires String Input
    bin = list(binthing)

    binary = len(bin) - 1  # 3
    total, power = 0, 0

    for i in reversed(range(0, binary + 1)):
        if bin[i] == "1":
            total += int(bin[i]) * 2 ** power
        power += 1
    return total


def IntToBinary(number):
    binary, count = [], int(number)
    while count > 0:
        r = count % 2
        binary.insert(0, str(r))
        count = count // 2

    return "".join(binary)


while True:
    print(BinaryToInt(input("Binary to Base 10>>> ")))
    print(IntToBinary(int(input("Base 10 to Binary>>> "))))
    input("") #Infinite Loop Pervention
