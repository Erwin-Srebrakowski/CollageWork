import sys

def display_menu():
    see_menu = input('Whould you like to see the menu?')

    if see_menu.lower() == 'y':
        menu = ['Margharita', 'Peperoni', 'Texas BBQ']
        print('Menu:')

        for i in range (len(menu)):
            print('{}. {}'.format(i + 1, menu[i]))

    else:
        print('Goodbye')
        sys.exit()

def choose_pizza():
    choose_food = input('You can type the frist letter of pizza you want')
    
    if (choose_food == 'm' or choose_food == 't' or choose_food == 'p'):
        print('Baking pizza')
    else:
        print('Please type m,p or t')

def pizza_ready():
    print('Pizza is ready')
    print('Enjoy')

def main():
    display_menu()
    choose_pizza()
    pizza_ready()





if __name__ == '__main__':
    main()