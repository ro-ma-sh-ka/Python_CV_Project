#find out number
import random

number = random.randint(1, 100)
attempts = {1: 10, 2: 5, 3: 3}
answer = 0
count = 0
level_game = int(input('Please choose the level of the game 1) easy; 2) difficult; 3) hard:'))

while answer != number and count < attempts[level_game]:
    count += 1
    answer = int(input(f'Step {count} from {attempts[level_game]}. Please enter your variant: '))
    if answer > number:
        print('your variant is bigger.')
    elif answer < number:
        print('your variant is less.')
if answer != number:
    print('You lost...')
else:
    print(f'You won from {count} step! Congratulations!')