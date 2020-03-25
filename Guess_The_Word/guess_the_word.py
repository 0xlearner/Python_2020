import random

print('Welcome to the Guess My Word Game')

game_dict = {
    "sports": ['basketball', 'baseball', 'soccer', 'football', 'tennis', 'curling'],
    "colors": ['orange', 'yellow', 'purple', 'aquamarine', 'violet', 'gold'],
    "fruits": ['apple', 'banana', 'watermelon', 'peach', 'mango', 'strawberry'],
    "classes": ['english', 'history', 'science', 'mathematics', 'art', 'health'],
}

game_keys = []
for key in game_dict.keys():
    game_keys.append(key)

playing = True
while playing:
    game_category = random.choice(game_keys)
    game_word = random.choice(game_dict[game_category])

    wrong = 0
    stages = ["",
              "________        ",
              "|               ",
              "|        |      ",
              "|        0      ",
              "|       /|\     ",
              "|       / \     ",
              "|               "
              ]
    r_letters = list(game_word)
    board = ['___'] * len(game_word)
    win = False
    guess_count = 0

    print(f'\nGuess a {len(game_word)} letter word fromt he following category:{game_category.title()}')
    while wrong < len(stages) - 1:
        print('\n')
        guess = input('Enter your guess: ')
        guess_count += 1
        if guess == game_word:
            print(f'\nCorrect! You guessed the word in {guess_count} guesses.')
            win = True
            break
        else:
            wrong += 1
        print(" ".join(board))
        wrong_guess = wrong + 1
        print('\n'.join(stages[0:wrong_guess]))

        for letter in random.choice(game_word):
            c_index = r_letters.index(letter)
            board[c_index] = letter
    if not win:
        print('\n'.join(stages[0:wrong]))
        print(f'You lose!It was {game_word}')

    playing = False



