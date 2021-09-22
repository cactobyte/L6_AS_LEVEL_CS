bird = input()

bird_count = [0,0,0,0]
bird_names = ["robin", "blackbird", "wren", "starling"]

while bird != "x":
    bird_Found = False
    numberOfSpecies = len(bird_names)

    for count in range(0, numberOfSpecies):
        if bird == bird_names[count]:
            bird_index = count
            bird_Found = True
            birds_observed = int(input("how many tho"))
            bird_count[count] = bird_count[count] + birds_observed
    if not(bird_Found):
        print(bird, "added to the bird species array")
        bird_names.append(bird)
        birds_observed = int(input("how many did u see"))
        bird_count.append(0)
        bird_count[numberOfSpecies] = bird_count[numberOfSpecies]+birds_observed
    bird = input()

for i in range(0, numberOfSpecies):
    print(bird_names[i],bird_count[i])

#### BIRD COUNT
