import random

number = random.randint(1, 100)
answer = 0

while answer != number:
    answer = int(input('please enter your variant: '))
    if answer > number:
        print('your variant is bigger. Try again.')
    elif answer < number:
        print('your variant is less. Try again')

print('You won! Congratulations!')