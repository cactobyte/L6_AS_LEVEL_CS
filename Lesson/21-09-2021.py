a = int(input())
b = int(input())

while a % b > 0:
    r = a % b
    a = b
    b = r
print(b)

# Euclids Algorithm, for finding two highest common multiples

bird = input().lower()
birdFound = False
birdName = ["robin", "blackbird", "magpie", "burd", "big burd", "big boi"]

for i in birdName:
    if i == bird:
        birdFound = True

if not(birdFound):
    print("Couldnt find bird")
else:
    print("Found bird")

# B U R D 

