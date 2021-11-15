# Making a tic, tac, toe game
import random
print("Welcome to my tic, tac,toe game !")
linet = ("|*|*|*|")
splay = True
#This is a while statement for playing or not the game 
while splay == True :
    print(linet)
    print(linet)
    print(linet)
    on = True
    while on == True :
        cel1 = "*"
        cel2 = "*"
        cel3 = "*"
        cel4 = "*"
        cel5 = "*"
        cel6 = "*"
        cel7 = "*"
        cel8 = "*"
        cel9 = "*"
        playy = True
        computer_choices = ["1","2","3","4","5","6","7","8","9", "null"]
        while playy == True :
            choice = input("On which square do you wish go ? :")
            if choice not in computer_choices :
                choice = input("Try again ! :")
            #I need to find out how to remove string from the list of choices
            if choice in computer_choices :
                if choice == "1" :
                    cel1 = "X"
                    computer_choices.remove(choice)
                if choice == "2" :
                    cel2 = "X"
                    computer_choices.remove(choice)
                if choice == "3" :
                    cel3 = "X"
                    computer_choices.remove(choice)
                if choice == "4" :
                    cel4 = "X"
                    computer_choices.remove(choice)
                if choice == "5" :
                    cel5 = "X"
                    computer_choices.remove(choice)
                if choice == "6" :
                    cel6 = "X"
                    computer_choices.remove(choice)
                if choice == "7" :
                    cel7 = "X"
                    computer_choices.remove(choice)
                if choice == "8" :
                    cel8 = "X"
                    computer_choices.remove(choice)
                if choice == "9" :
                    cel9 = "X"
                    computer_choices.remove(choice)
#DEBUBG            print(computer_choices)
            computer_choice = random.choice(computer_choices)
            # Very Important the 2 lines down
            if computer_choice in computer_choices :
                computer_choices.remove(computer_choice)
                computer_choices.append("null")
                computer_choices.remove("null")
#            print(computer_choice)
#            print(computer_choices)
            while computer_choice == "null" :
                computer_choice = random.choice(computer_choices)
            if computer_choice == "1" :
                cel1 = "0" 
            if computer_choice == "2" :
                cel2 = "0"
            if computer_choice == "3" :
                cel3 = "0" 
            if computer_choice == "4" :
                cel4 = "0"
            if computer_choice == "5" :
                cel5 = "0" 
            if computer_choice == "6" :
                cel6 = "0"
            if computer_choice == "7" :
                cel7 = "0" 
            if computer_choice == "8" :
                cel8 = "0"
            if computer_choice == "9" :
                cel9 = "0"        
            line1 = ("|" + cel1 + "|" + cel2 + "|" + cel3 + "|")
            line2 = ("|" + cel4 + "|" + cel5 + "|" + cel6 + "|")
            line3 = ("|" + cel7 + "|" + cel8 + "|" + cel9 + "|")
            print(line1)
            print(line2)
            print(line3)
            if cel3 == cel6 == cel9 == "X":
                print("You won !")
                playy = False   
            if cel2 == cel5 == cel8 == "X":
                print("You won !")
                playy = False   
            if cel1 == cel4 == cel7 == "X":
                print("You won !")
                playy = False  
            if cel1 == cel2 == cel3 == "X":
                print("You won !")
                playy = False   
            if cel4 == cel5 == cel6 == "X":
                print("You won !")
                playy = False   
            if cel7 == cel8 == cel9 == "X":
                print("You won !")
                playy = False 
            if cel3 == cel5 == cel7 == "X":
                print("You won !")
                playy = False
            if cel1 == cel5 == cel9 =="X":
                print("You won !")
                playy = False
            if cel3 == cel6 == cel9 == "0":
                print("You lost !")
                playy = False   
            if cel2 == cel5 == cel8 == "0":
                print("You lost !")
                playy = False   
            if cel1 == cel4 == cel7 == "0":
                print("You lost !")
                playy = False  
            if cel1 == cel2 == cel3 == "0":
                print("You lost !")
                playy = False   
            if cel4 == cel5 == cel6 == "0":
                print("You lost !")
                playy = False   
            if cel7 == cel8 == cel9 == "0":
                print("You lost !")
                playy = False 
            if cel3 == cel5 == cel7 == "0":
                print("You lost !")
                playy = False
            if cel1 == cel5 == cel9 =="0":
                print("You lost !")
                playy = False
            if cel1 != "*" and cel2 != "*" and cel3 != "*" and cel4 != "*" and cel5 != "*" and cel6 != "*" and cel7 != "*" and cel8 != "*" and cel9 != "*" :
                print("It's a tie")
                playy = False
# You still need to add a removeal of cells from the list after all choices !