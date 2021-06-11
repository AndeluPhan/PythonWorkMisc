import random
from WordBank import MostAmazingParser

def DisplayHangman(errors):
    hangman = ['''====]
    |





_____________''',
    '''====]
    |
    O




_____________''',
        '''====]
    |
    O
    |



_____________''',
        '''====]
    |
    O
   /|



_____________''',
        '''====]
    |
    O
   /|\ 



_____________''',
        '''====]
    |
    O
   /|\ 
    |


_____________''',
        '''====]
    |
    O
   /|\ 
    |
   / 

_____________''',
        '''====]
    |
    O
   /|\ 
    |
   / \ 

_____________''']
    for i in range(0,8,1):
        if i == errors:
            print(hangman[i])

def GameMechanics(WordList, Original, letter, turn):
    global errorOrNot
    errorOrNot = 1
    Size = 0
    for i in WordList:
        Size += 1
    for i in range(0,Size, 1):
        if turn == 0:
            if Original[i] != " ":
                WordList[i] = "_ "
        else:
            if Original[i] == letter:
                WordList[i] = letter
                errorOrNot = 0
    return WordList
errorOrNot = 0 
def RepetitionCheck(letterChoices, letter,turn):
    if turn > 0:
        for i in letterChoices:
            #print("i : " + i)
            #print("vocab: " + ', '.join(letterChoices))
            #print("letter: " + letter)
            if letter == i:
                print("\n***You've already used that selection. Please try again!***\n ")
                return True
    return False
def CheckforWin(original, CurrList):
    #if current list matches original list, then player has won. 
    for f,b in zip(original, CurrList):
        if f != b:
            return False
    return True
def AsktoPlayAgain(guess,Gameon):
    answer = None
    while True:
        try:
            answer = str(input("\nWould you like to play again? (y/n): "))
        except ValueError:
            print("Please enter either y for yes, or n for no (y/n)")
        if answer.lower() not in ('y','n'):
            print("Please enter either y for yes, or n for no (y/n)")
        else:
            break
    if answer == "y":
        print("Let's go again!\n")
        return True
    else:
        print("Thank for playing! Please let Andrew know how you feel about this game. Feedback is greatly appreciated.")
        Gameon = False
        return False
    return True
def RandomWord():
    HugeList = MostAmazingParser()
    RandomNum = random.randint(0,len(HugeList))
    return HugeList[RandomNum]
def Manual():
    boolean = True
    while boolean:
        manualans = input("Quickly give a word or type 'break' to back to earlier selection: ").lower()
        for i in manualans:
            if i not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ','break'):
                print("Invalid entry for manual input. Try Again.")
            else:
                return manualans
def ManualOrRandom():
    print("Would you like your word to be manual, random or impossible?")
    choice = None
    Valid = True
    while Valid:
        print("**You can only play impossible once. Since its my favorite word for this game.**")
        choice = input("m for manual, r for random or i for impossible (m/r/i): ")
        print("choice: " + choice)
        if choice != 'm' and choice != 'r' and choice != 'i':
            print("please choose between 'm' or 'r'or 'i'")
        if choice == 'm':
            ManualAns = Manual()
            if ManualAns == 'break':
                continue
            else:
                print("Printing lines so players can't see...")
                for i in range(0,60,1):
                    print("")
                return ManualAns
        else: 
            break

    if choice == 'i':
        return "jazz"
    else:
        return RandomWord()
def GuessWord(Origin, Guess):
    GuessList = list(Guess)
    if GuessList != Origin:
        print("Sorry, your guess was wrong\n")
        return False
    else:
        print("Congratulations, you are correct!\n")
        return True
def Printinstructions():
    print("Welcome to Andrew's Hangman Game. The following are instructions:\n")
    print("1)First select whether you would like your word to be manual or random. Random pulls a word from the internet, and Manual is self-entered.")
    print("***NOTE: For manual, tell player 2 or 3 to close eyes briefly so that you can input a word choice. Give only valid words")
    print("2) You can guess letters but not numbers or anything else. ")
    print('3) Type "guess" when you want to just straight guess the word.')
    print("4) You can keep guessing until all the body parts of Timothy appear on the screen. If you can guess the word before that happens you win.")
    print('5) Follow all on screen directions and have fun! Feedback on the game would also be amazing! Thank you\n')
    return
def PlayGame():
    Printinstructions()
    name = input("Timothy's soul is in your hands \nWhat's your name: ")
    print("\nWelcome " + name + " let's start!")
    GameOn = True
    Wins = 0
    NumberGames = 0
    while GameOn:
        #Step 1: The word is chosen. (Manual Selection or Random)
        
        ChosenWord = ManualOrRandom()
        #ChosenWord = "testing" #for testing purposes
        turn = 0
        #Step 2: Display both the hangman and the number of dashes. 1 dash per letter. 
        ChWordList = list(ChosenWord)  #ChWordList continually changes, while we constantly compare to Original (List) which doesnt. 
        Original = ChWordList.copy()
        DisplayHangman(0)
        print()
        print(' '.join(GameMechanics(ChWordList,Original,"a",turn)))
        print()
        guess = True
        errorCount = 0
        letterChoices = set()
        while guess:
            turn += 1
            print("Previous guesses: " + ', '.join(letterChoices))
            print("Number of bad choices: " + str(errorCount))
            letChoice = input("\nGuess a letter in this word: ").lower()
            if letChoice not in ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','guess'):
                print('Invalid Choice. Please choose either a letter or type "guess" to guess')
            print("___________________________________________________________\n")
            #Step 3 Implement the Option to guess
            if letChoice == "guess":
                guess = input("What's your guess?: ")
                if not GuessWord(Original, guess): #If the guess was wrong
                    errorCount += 1
                    DisplayHangman(errorCount)
                    continue
                else:
                    NumberGames += 1
                    Wins += 1
                    print("The word was: " + ChosenWord)
                    print(name + " has saved Timothy from certain death! \n You Win!")
                    guess = False
            #Check for repetition, if word was already pass the rest of the loop and try again. 
            if RepetitionCheck(letterChoices, letChoice,turn):
                continue
            letterChoices.add(letChoice)
            Templist = GameMechanics(ChWordList,Original, letChoice, turn).copy()
            if guess: #This fixes the bug so that guessing does not count as a wrong selection.
                errorCount += errorOrNot
            DisplayHangman(errorCount)
            print()
            print(' '.join(GameMechanics(ChWordList,Original,letChoice,turn)))
            print()
            #implement checks for whether the player has won or lost. 
            if CheckforWin(Original, ChWordList):
                print("The word was: " + ChosenWord)
                print("\nYou have saved Timothy from the shadow realm. \nYou Win!")
                NumberGames += 1
                Wins += 1
                guess = False
            elif errorCount == 7:
                NumberGames += 1
                print("The word was: " + ChosenWord)
                print("\nTimothy's soul has been sent to the shadow realm. \nYou Lose!")
                guess = False
            #Ask player whether or not they want to play again
            if guess == False:
                reply = AsktoPlayAgain(guess, GameOn)
            #print(reply) #if player says y, the break out of this loop and continue
                if not reply:
                    GameOn = False
                    break
                else:
                    GameOn = True
                    break
        print()
        print("You have won and saved Timothy " + str(Wins) + "/" + str(NumberGames) + " times.")
        print()


            


#Must Check for repetition of words, and also if the player wins or loses. 
#Must implement a guessing function
#Must implement a function to let player play again if they wish to. 


PlayGame()