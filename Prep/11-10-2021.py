# Players inputing name
player1 = input("Player One, please input your name>> ")
player2 = input("Player Two, please input your name>> ")

player1_wins = 0
player2_wins = 0

playerWon = False

allWins = {  # Each item and what it can be beaten by
    "r": "p",
    "s": "r",
    "p": "s",
}

while not playerWon:
    player1_input = input(
        "{}, what is your choice between ROCK (R), PAPER (P) and SCISSORS (S)>> ".format(player1)).lower()
    player2_input = input(
        "{}, what is your choice between ROCK (R), PAPER (P) and SCISSORS (S)>> ".format(player2)).lower()

    if player1_input == player2_input:
        print("That's a draw")
    else:
        if player1_input in allWins:
            if player2_input in allWins[player1_input]:
                print(player2, " wins")
                player2_wins += 1
            else:
                print(player1, " wins")
                player1_wins += 1

    print("Current Score: {} {} and {} {}".format(player1, player1_wins, player2, player2_wins))

    if player1_wins > 2 or player2_wins > 2:
        playerWon = True
        if player1_wins > player2_wins:
            print("Congratulations {}, you won with {} wins".format(player1, player1_wins))
        else:
            print("Congratulations {}, you won with {} wins".format(player2, player2_wins))
