#find out number
import random

number = random.randint(1, 100)
attempts = {1: 10, 2: 5, 3: 3}
answer = 0
count = 0
qty_players = int(input('How many players will play:'))
names = {i: input(f'Input {i} name: ') for i in range(1, qty_players+1)}

level_game = int(input('Please choose the level of the game 1) easy; 2) difficult; 3) hard:'))

while answer != number and count < attempts[level_game]:
    count += 1
    print(f'Step {count} from {attempts[level_game]}')
    values = {i: int(input(f'{names[i]} enter your variant: ')) for i in range(1, qty_players+1)}

    for i in values:
        if values[i] > number:
            print(f'{names[i]}, your variant is bigger.')
        elif values[i] < number:
            print(f'{names[i]}, your variant is less.')
        else:
            answer = values[i]
            print(f'{names[i]}, you won from {count} step! Congratulations!')
if answer != number:
    print(f'Answer is {number}. You lost...')