import random

print('-' * 30)
print('GUESS THAT NUMBER'.center(30))
print('-' * 30 + '\n')

the_number = random.randint(1, 100)
guess_number = False
player_name = input('What is your name? ')

while guess_number != the_number:
    guess_number = int(input('Guess a number between 1 to 100: '))

    if guess_number < the_number:
        print(f'Sorry,{player_name.title()} your guess of {guess_number} is too low.')
    elif guess_number > the_number:
        print(f'Sorry,{player_name.title()} your guess of {guess_number} is too high.')
    else:
        print(f'Congrats {player_name.title()}! you won!!')