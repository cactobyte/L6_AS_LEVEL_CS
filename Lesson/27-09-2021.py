number_of_moves = 0
board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

def printBoard():
    for x in range(0, 3):
        for y in range(0, 3, 3):
            print("{} | {} | {}".format(board[x][y], board[x][y+1], board[x][y+2]))

def changeBoard(symbol, index):
    if board[index//3][index%3] == "-":
        board[index//3][index%3] = symbol
    else:
        print("Your move was invalid")

def demoBoard():
    print("\n1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9\n")


while number_of_moves <= 6:
    demoBoard()
    x = int(input(">>>"))
    changeBoard("x", x-1)
    printBoard()
    y = int(input(">>>"))
    changeBoard("o", y-1)
    printBoard()

    
### Tic Tac Toe without win check
