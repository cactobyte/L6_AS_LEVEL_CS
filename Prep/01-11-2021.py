def strToBinary(binthing):
    bin = list(binthing)

    binary = len(bin) - 1 #3
    total, power = 0, 0
    
    for i in reversed(range(0, binary+1)):
        if bin[i] == "1":
            total = total + int(bin[i])*2**power
        power += 1
    return(total)
