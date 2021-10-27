'''
Ask user to enter their name and then ask to enter a numer.
If the number is under 5 disply 'Hello [name]'.
If the number is over 5 display 'Hi [name]' otherwise display 'Howdy [name]'.
'''


name = input('enter your name\n')
number = int(input('enter a number\n'))
if number < 5:
    print('Hello ' + name)
elif number > 5:
    print('Hi ' + name)
else:
    print('Howdy ' + name)