import random

print('Guess my Number')

user = input('\nHello!What is your name > ')

print(f'Well!{user} i am thinking of a number between 1 to 20.')
number = random.randint(1,20)

for guess_num in range(5):
    guess = int(input('\nTake a Guess >'))

    if guess< number:
        print('Your Guess is too Low')
    elif guess > number:
        print('Your Guess is too High')
    else:
        break

if guess == number:
    print(f'Good job! {user} you guessed my number in {guess_num+1} guesses!')
else:
    print(f'\nGame Over...The number I was thinking of was {number}.')