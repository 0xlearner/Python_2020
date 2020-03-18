import random

rounds = int(input('How many Rounds would you like to play: '))
player_score = 0
computer_score = 0
ties = 0

beats = {
    'rock':'scissor',
    'paper':'rock',
    'scissor':'paper'
}
choices = ['rock','paper','scissor']

for game_round in range(rounds):
    print(f'\nRound> {game_round+1}')
    print(f'Player Score:{player_score}\tComputer Score:{computer_score}\tTies:{ties}')

    player_choice = input("Time to pick...rock, paper, scissors: ").lower().strip()


    if player_choice in choices:
        computer_choice = random.choice(choices)
        print(f'Computer choose {computer_choice}')
        #Game Logic
        if player_choice == computer_choice:
            ties += 1
            print(f"It's a tie.{player_choice}=={computer_choice}")
        elif beats[player_choice] == computer_choice:
            player_score += 1
            print(f'You Win Round {game_round+1}!!! {player_choice} beats {computer_choice}')
        else:
            computer_score += 1
            print(f'You Lose...Computer wins Round {game_round+1} {computer_choice} beats {player_choice}')
    else:
        print('Not a valid move.')
        print('Computer gets a point.')
        computer_score += 1

print("\nFinal Game Results")
print(f"\tRounds Played: {rounds}")
print(f"\tPlayer Score: {player_score}")
print(f"\tComputer Score: {computer_score}")
print(f"\tTies: {ties}")
if player_score > computer_score:
    print(f'\tWinner is Player!!!')
elif computer_score > player_score:
    print('\tWinner is Computer')
else:
    print('\tThe game was a tie.')




