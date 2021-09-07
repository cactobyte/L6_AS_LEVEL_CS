# QUESTION TWO

bill = int(input())
total = int(input())
print(round(bill*1.1 / total))

# QUESTION THREE

one_penny = int(input("Amount of 1p: "))
two_pence = int(input("Amount of 2p: "))
five_pence = int(input("Amount of 5p: "))
ten_pence = int(input("Amount of 10p: "))
twenty_pence = int(input("Amount of 20p: "))
fifty_pence = int(input("Amount of 50p: "))

total_pence = one_penny + two_pence*2 + five_pence*5 + ten_pence*10 + twenty_pence*20 + fifty_pence*50
# Calculates total amount of pennies
money = total_pence / 100 # Converts to pounds

print("You have a total of {} pence, which is {} pounds".format(total_pence, money))

# QUESTION FOUR

vatRate = 20
netPrice = int(input("Enter net price: "))
amountOfVat = netPrice * vatRate / 100

priceWithVat = netPrice +  amountOfVat
print("{} \n{}".format(amountOfVat, priceWithVat))
