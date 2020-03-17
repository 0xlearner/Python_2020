import random

print('Welome to Coin Toss Program')

print('I will flip a coin a set number of times.')

#Get user_input
flip_number = int(input('How many times you would like me to flip the coin > '))
choice = input('Would you like to see the result of each flip(y/n) > ')

print('\n!!!Flipping!!!')

#Initialize variables
heads = 0
tails = 0

#The main loop
for flips in range(flip_number):
    coin = random.randint(0,1)
    if coin == 1:
        heads += 1
        if choice.startswith('y'):
            print('HEADS')
    else:
        tails += 1
        if choice.startswith('y'):
            print('TAILS')
    if heads == tails:
        print(f'At {flips+1} flips,the number of heads and tails were equal at {heads} each.')

#Calculate the Percentages
heads_percentage = round(100*heads/flip_number,2)
tails_percentage = round(100*tails/flip_number,2)

#Printing the Result
print(f'Results Flipping a coin {flip_number} number of times:')
print('\nSide\t\tCount\t\tPercentage')
print(f'Heads\t\t {heads} / {flip_number}\t\t {heads_percentage}%')
print(f'Tails\t\t {tails} / {flip_number}\t\t {tails_percentage}%')
