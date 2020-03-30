import random


def sides():
    """Ask the user how many sides on their die"""
    side = int(input('\nHow many sides would you like on your dice: '))
    return side


def no_of_rolls():
    """Ask the user number of rolls they want to roll"""
    number_of_rolls = int(input('How many dice would you like to roll: '))
    return number_of_rolls


def roll_dice(sides, number):
    """Simulate rolling the dice"""
    dice = []
    print(f'You rolled {number} times with {sides} sided dice. ')
    print('\n-----Results are as followed-----')
    for _ in range(number):
        value = random.randint(1, sides)
        print(f'\t {value}')
        dice.append(value)
    return dice


def sum_dice(dice):
    """Add all the values of dice in a list"""
    total = 0
    for die in dice:
        total += die
    print(f'The total value of your roll is {total}.')


def roll_again():
    """Ask the user to roll again"""
    choice = input('\nWould you like to roll again [y/n]: ')
    if choice != 'y':
        roll = False
    else:
        roll = True
    return roll

# The main code
print('Welcome to Dice Game')

rolling = True
while rolling:
    # Get the user info for the typ of dice
    d_sides = sides()
    d_number = no_of_rolls()

    # Roll and sum the dice
    dice_roll = roll_dice(d_sides,d_number)
    sum_dice(dice_roll)

    #Roll again
    rolling = roll_again()

print('\nThank you for playing.')