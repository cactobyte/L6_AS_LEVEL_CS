fibonacci = []
# 1 1 2 3 5 8
def generate_fibon(numbers):
    fibon = [1, 1,]
    for i in range(0, numbers-2):
        fibon.append(fibon[i] + fibon[i+1])
    return fibon

fibonacci = generate_fibon(1000)
print(fibonacci)

digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
digit_count = [0, 0, 0, 0, 0, 0, 0, 0, 0]
for i in fibonacci:
    x = str(i)
    first_digit = int(x[0])

    for y in digits:
        if y == first_digit:
            digit_count[y-1] += 1

print(digit_count)
