todo_list = []
def list():

    operation = input('''Select operation:\n [1] Add input to the to-do list \n [2] Remove input from the to-do list \n [3] Display list\n ''')


    if operation == '1':
        print("Type the input you would like to add to the to-do list: ")
        userinput = str(input())
        todo_list.append(userinput)

    elif operation == '2':
        print("Type position of the element input you like to remove from the to-do list: ")
        userinput = str(input())
        todo_list.pop(userinput)

    elif operation == '3':
        for todo in todo_list:
            if 'buy' or todo == 'Buy':
                print(todo,"$$$")
            #If string contains the text "buy" append 3 dollar strings at the end
            print("Jarvis is going to:",todo)

    else:
        print('You have not chosen a valid operator, please run the program again.')

    again()

def again():
    list_again = input('''Would you like to see main menu again? (Y/N)''')

    if list_again.upper() == 'Y':
        list()
    elif list_again.upper() == 'N':
        print('OK. Bye bye. :)')
    else:
        again()

list()