def crypt(msg, shift):
    yeet = []
    for letter in msg:
        yeet += chr(ord(letter) + shift)
    return yeet 


def coolcrypt(message, shift):
    yeet = []
    for letter in message:
        yeet += chr(ord(letter) + shift)
    return "".join(yeet)


decrypt = ['f', 'q', 'g', 'u', 'p', 'v', '"', 'o', 't', '"', 'i', 'q', 'q', 'f', 'j', 'g', 'c', 'f', '"', 'n', 'k', 'm',
           'g', '"', 'n', 'k', 'm', 'g', '"', 'f', 't', '"', 'r', 'j', 'k', 'n']
message = "".join(decrypt)

for i in range(-26, 26):
    print(coolcrypt(message, i))

print(crypt("8====D", -2))
