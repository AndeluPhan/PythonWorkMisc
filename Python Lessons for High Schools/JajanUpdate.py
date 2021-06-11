import random

list = ['rock','paper','scissor']
Player = True
while(Player):
    computer = list[random.randint(0,2)]
    playerAns = input('choose: rock, paper or scissor? ')
    if playerAns == 'quit' or playerAns == 'Quit':
        Player = False
        break
    elif playerAns != 'rock' and playerAns != 'paper' and playerAns != 'scissor':
        print('typo: try again!')
        continue
    elif computer == playerAns:
        print("It's a tie!")
        print("You chose:", playerAns, "computer chose: ",  computer)
    elif computer == 'paper':
        if playerAns == 'rock':
            print("Computer Wins! You chose", playerAns, "and the computer chose",computer)
        elif playerAns == 'scissor':
            print("You Win! You chose", playerAns, "and the computer chose", computer)
    elif computer == 'rock':
        if playerAns == 'paper':
            print("You Win! You chose", playerAns,"and the computer chose",computer)
        elif playerAns == 'scissor':
            print("Computer Wins! You chose", playerAns,"and the computer chose" , computer)
    elif computer == 'scissor':
        if playerAns == 'rock':
            print("You Win! You chose", playerAns, "and the computer chose" , computer)
        else:
            print("Computer Wins! You chose", playerAns, "and the computer chose" , computer)
    else:
        print("typo, try again...")
        
