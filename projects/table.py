# Making a program that writes tables 
# Could merge this table generarator with the tic tac toe game (maybe)
print("Welcome to the table creator !")
rows = input("How many rows do wish to have for your table ? :")
columns = input("How many columns do you wish to have for your table ? :")
a = 1
b = 1
tab = "|X|"
while b < int(columns) :
    tab = tab + "X|"
    b = b + 1
while a <= int(rows) :
    print(tab)
    a = a + 1
