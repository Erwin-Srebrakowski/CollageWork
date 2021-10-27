'''
Ask the user for thir age.
If they are 18 or older, tell them 'You can vote'.
If they are 17, tell them 'you can learn to drive'.
If they are 16, tell them 'You can buy a lottery ticket'
and for everybody else display the message
'Nobody looks at you strangely if you do a catwheel in public'
'''



def main():
    number = int(input('enter your age\n'))
    if number >= 18:
        print('you can vote')
    elif number == 17:
        print('you can learn to drive')
    elif number == 16:
        print('you can buy a lottery ticket')
    else:
        print('nobody looks at you strangely if you do a catwheel in puplic')


if __name__ == '__main__':
    main()