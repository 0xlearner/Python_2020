import random

print('-' * 30)
print('GUESS THAT NUMBER'.center(30))
print('-' * 30 + '\n')

the_number = random.randint(1, 100)
guess_number = False

while guess_number != the_number:
    guess_number = int(input('Guess a number between 1 to 100: '))

    if guess_number < the_number:
        print('Too Low')
    elif guess_number > the_number:
        print('Too High')
    else:
        print('You Win!')