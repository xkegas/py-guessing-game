import os
from time import sleep
class GuessingGame:
    def __init__(self):
        print("Welcome to the game!")
        self.p1 = ""
        self.p1_word = ""
        self.p2 = ""
        self.p2_word = ""
        self.setupGame()

    def setupGame(self):
        p1Name = input("Enter name of Player 1: ")
        p2Name = input("Enter name of Player 2: ")
        self.UpdateNames(p1Name, p2Name)
        self.P1Turn()

    def ValidateNames(self, p1, p2):
        if(p1 == p2):
            print("Choose different names!")
            return 0
        else:
            return 1

    def UpdateNames(self, p1Name, p2Name):
        if(self.ValidateNames(p1Name, p2Name) != 1):
            self.setupGame()
        self.p1 = p1Name
        self.p2 = p2Name

    def P1Turn(self):
        os.system('cls')
        print(self.p1 + "'s turn: ")
        input(self.p2 + " that's not for you! (Enter to continue)")
        print("slowo p1: " + self.p1_word)
        if(self.p1_word == ""):
            self.p1_word = input("Type a word which enemy has to guess: ")
            self.P2Turn()
        else:
            Guess = input("Guess enemy's word: ")
            if(Guess == self.p2_word):
                self.Win(self.p1, self.p2_word)
            else:
                print("No!")
                sleep(1)
                self.P2Turn()

    def P2Turn(self):
        os.system('cls')
        print(self.p2 + "'s turn: ")
        input(self.p1 + " that's not for you! (Enter to continue)")
        if (self.p2_word == ""):
            self.p2_word = input("Type a word which enemy has to guess: ")
            self.P1Turn()
        else:
            Guess = input("Guess enemy's word: ")
            if (Guess == self.p1_word):
                self.Win(self.p2, self.p1_word)
            else:
                print("No!")
                sleep(1)
                self.P1Turn()

    def Win(self, whoWon, word):
        os.system('cls')
        print("You won!\n" + "Congratulatons, " + whoWon)
        print("It was: " + word)
        self.Again()

    def Again(self):
        choice = input("Want to play again? y/n")
        if(choice != 'y'):
            print("Goodbye!")
            exit(0)
        else:
            self.p1_word = ""
            self.p2_word = ""
            self.setupGame()





