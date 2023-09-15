def user_choice():
    choice = 'wrong'
    acceptable_range = (0,10)
    within_range = False
    while(choice.isdigit() == False or within_range == False):
        choice =   input ('enter the number(0- 10)')
        if choice.isdigit() == False:
            print('not an integer')
        if choice.isdigit():
            if choice in acceptable_range:
                within_range = True
            else:
                within_range  = False
    return choice
print(user_choice()) 