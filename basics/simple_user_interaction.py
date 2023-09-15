game_list = [0,1,2]
def display(game_list):
    print("current list")
    print(game_list)
def position_choice():
    choice = 'wrong'
    while choice not in ['0','1','2']:
        choice = input("enter the position")
        if choice not in ['0','1','2']:
            print("invalid choice")
    return int(choice)
def repalcement(game_list, position):
    user_placement = input ("place at positon ")
    game_list[position] = user_placement
    return game_list
def gameon():
    choice = 'wrong'
    while choice not in ['Y','N']:
        choice = input("keep playing (Y OR N)")
        if choice not in ['Y','N']:
            print("please chose Y or N")
    if choice == "Y":
        return True
    else:
        return False
game_on = True
game_list = [0,1,2]
while game_on:
    display(game_list)
    postion = position_choice()
    repalcement(game_list,postion)
    display(game_list)
    game_on = gameon()
