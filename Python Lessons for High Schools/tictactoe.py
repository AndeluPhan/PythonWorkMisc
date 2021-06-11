board = ["_","_","_",
        "_","_","_",
        "_","_","_"]

def displayBoard():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])

def play_game():
    game = True
    incorrect = True
    first_player = None
    print("Welcome to Andrew's Tic Tac Toe. Let's go!")
    print("This is the board:")
    print("1 | 2 | 3")
    print("4 | 5 | 6")
    print("7 | 8 | 9")
    while incorrect:
        first_player = input("Who would like to go first? 'O' or 'X'?: ")
        if first_player == "O" or first_player == "X":
            incorrect = False
        else:
            print("Incorrect Option. Try Again.")
    print("First Player: " + first_player)
    NumRounds = 1
    while game:
        handle_turn(NumRounds, first_player)
        game = checkforWin(game, Curr_player(first_player, NumRounds))
        if game != False:
            game = checkforTie(NumRounds, game, first_player)
        NumRounds += 1
    
def handle_turn(RoundNum, first_PLAYER):
    if RoundNum > 1:
        print("Player " + Curr_player(first_PLAYER, RoundNum) + " is now playing...")
    currPos = True
    while currPos:
        position = input("Choose a position from 1-9: ")
        if position not in ["1","2","3","4","5","6","7","8","9"]:
            print("Invalid Position Number. Choose Another.")
        elif board[int(position) -1] == "_":
            currPos = False
            board[int(position) -1] = Curr_player(first_PLAYER, RoundNum)
        else:
            print("Invalid Position: This Spot has already been taken. ")
    displayBoard()

def checkforWin(Game, currplayer):
    #check for columns
    #print("checking...")
    GameWin = True
    for i in range(0,3,1):
        #print("in the loop")
        if board[i] == board[i + 3] and board[i+3] == board[i+6]:
            if board[i] != "_" or board[i+3] != "_" or board[i+6] != "_":
                print("Player " + currplayer + " has the bigger pp today")
                GameWin = False
    #check for rows

    for j in range(0,8,3):
        if board[j] == board[j+1] and board [j+1] == board[j+2]:
            if board[j] != "_" or board[j+1] != "_" or board[j+2] != "_":
                print("Player " + currplayer + " has the bigger pp today")
                GameWin = False
    #check for diagonals
    if board[0] == board[4] and board[4] == board[8]:
        if board[0] != "_" or board[4] != "_" or board[8] != "_":
            print("Player " + currplayer + " has the bigger pp today")
            GameWin = False
    elif board[2] == board[4] and board[4] ==board[6]:
        if board[2] != "_" or board[4] != "_" or board[6] != "_":
            print("Player " + currplayer + " has the bigger pp today")
            GameWin = False
    return GameWin

def checkforTie(RoundNumber,game,first_PLAYER):
    #if board is filled, and no player has won then it's a tie. 
    #Tie checker should start working at a certain point of the game. 
    SimBoard = board
    if RoundNumber > 6:
        for i in SimBoard:
            if i != "_":
                i = Curr_player(first_PLAYER,RoundNumber)
                if checkforWin(game,Curr_player(first_PLAYER, RoundNumber)) == False: #if there is a possible win, then there can not be a tie. 
                    return True
                else: #if there is no possible win, then that is a tie. 
                    print("It's going to be a tie!")
                    return False
                i = "_"
    return True

def Curr_player(first_PLAYER, CurrRound):
    second_PLAYER = None
    if first_PLAYER == "X":
        second_PLAYER = "O"
    elif first_PLAYER == "O":
        second_PLAYER = "X"

    if CurrRound % 2 == 1:
        return first_PLAYER
    elif CurrRound % 2 == 0:
        return second_PLAYER

#bugs: game keeps returning true when printed. 

play_game()
