# Making a rock, paper, scissors game
import random
state = ["rock", "paper", "scissors"]
play = "Yes"
while play == "Yes" : 
    player_choice = input(" Plese chose from one of these three options " + str(state) + " :")
    computer_choice = random.choice(state)
    print(computer_choice)
    if player_choice == computer_choice :
        play = input("It's a tie ! Do you wish to continue ? Yes/No :")
    if player_choice != computer_choice :
        if player_choice == "rock" :
            if computer_choice == "paper" :
                play = input("You lost ! Do you wish to continue ? Yes/No :")
            if computer_choice == "scissors" :
                play = input("You won ! Do you wish to continue ? Yes/No :")
        if player_choice == "paper" :
            if computer_choice == "rock" :
                play = input("You won ! Do you wish to continue ? Yes/No :")
            if computer_choice == "scissors" :
                play = input("You lost ! Do you wish to continue ? Yes/No :")
        if player_choice == "scissors" :
            if computer_choice == "rock" :
                play = input("You lost ! Do you wish to continue ? Yes/No :")            
            if computer_choice == "paper" :
                play = input("You won ! Do you wish to continue ? Yes/No :")
