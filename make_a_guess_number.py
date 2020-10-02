import random

your_number = int(input("Please put your number from 0 to 100. I won't peep, trust me;)"))

start_position = 0
end_position = 100
comp_number = None
counter = 0

while comp_number != your_number:
    counter += 1
    comp_number = random.randint(start_position, end_position)
    comparation = input(f'My variant is:{comp_number}. Am I right or my number is more or less? (r/m/l):')
    if comparation == 'm':
        end_position = comp_number
    elif comparation == 'l':
        start_position = comp_number

print(f'I guessed it on {counter} attempts')
