bird_file = open("birdfile", "a+")

numrecs = int(input("How many records do you wish to write?"))

for n in range(1, numrecs + 1):
    bird_name = input("Enter bird name: ")
    birds_reported = input("Enter number of birds reported")

    bird_file.write("{}: {}\n".format(bird_name, birds_reported))

bird_file.close()

bird_file = open("birdfile", "r+")
for line in bird_file:
    print(line)

bird_file.close()
