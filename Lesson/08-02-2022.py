denary_number = int(input("gimme a number from -128 to 127: "))

binary_number = format(denary_number, "b")
while len(binary_number) < 8:

    binary_number = '0' + binary_number

    inverse_bin = ''
for i in binary_number:

    if i == '0':
        inverse_bin += '1'

    else:
        inverse_bin += '0'

n2 = '00000000'

carry = 0
result_string = ""
for i in range(7, -1, -1):
    n1_v = int(inverse_bin[i])
    n2_v = int(n2[i])

    b_sum = n1_v + n2_v + carry

    if b_sum == 0:
        result_string = "0" + result_string
        carry = 0
    elif b_sum == 1:
        result_string = "1" + result_string
        carry = 0
    elif b_sum == 2:
        result_string = "0" + result_string
        carry = 1
    elif b_sum == 3:
        result_string = "1" + result_string
        carry = 1

print(result_string)

import timeit

timeit.default_timer()
