# Program that shows the age of a person based on the calendar date that has been provided by the user input
# I am gonna set a manual date, for now atleast. Going to put an automated date sync (don't know in what kind of data format)
today_date = str("15/09/2021")
user_name = input("Please provide your name: ")
user_birthday = input("Please provide your birthday following the exemple \" " + today_date + "\" : ")
year = int(user_birthday[6] + user_birthday[7] + user_birthday[8] + user_birthday[9])
month_b = int(user_birthday[3] + user_birthday[4])
month_t = int(today_date[3] + today_date[4])
if month_b == month_t :
    if int(today_date[0] + today_date[1]) > int(user_birthday[0] + user_birthday[1]) :
        offset = 0
    else :
        offset = -1
    if int(today_date[0] + today_date[1]) == int(user_birthday[0] + user_birthday[1]) :
        offset = 0
        print(str(int(today_date[6] + today_date[7] + today_date[8] + today_date[9])-year + offset) + " years is your age, " + user_name + " ! Happy Birthday !")
    else :
        offset = -1
        print(str(int(today_date[6] + today_date[7] + today_date[8] + today_date[9])-year + offset) + " years is your age, " + user_name + " !")
if month_b != month_t :
    if month_b < month_t :
        offset = 0
        print(str(int(today_date[6] + today_date[7] + today_date[8] + today_date[9])-year + offset) + " years is your age, " + user_name + " !")
    else :
        offset = -1
        print(str(int(today_date[6] + today_date[7] + today_date[8] + today_date[9])-year + offset) + " years is your age, " + user_name + " !")
# As of 15/09/2021 the programs seems to be working properly