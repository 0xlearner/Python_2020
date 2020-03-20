import random

print('Welcome to the Thesaurus App!')

thesaurus = {
    "hot":['balmy', 'summery', 'tropical', 'boiling', 'scorching'],
    "cold":['chilly', 'cool', 'freezing', 'frigid', 'polar'],
    "happy":['content', 'cheery', 'merry', 'jovial', 'jocular'],
    "sad":['unhappy', 'downcast', 'miserable', 'glum', 'melancholy'],
}

print('\nHere are the words in thesaurus:')
for key in thesaurus.keys():
    print(f'\t-{key}')

choice = input('What word would you like a synonym for: ').lower().strip()

if choice in thesaurus.keys():
    synonym  = random.choice(thesaurus[choice])
    print(f'A synonym for {choice} is {synonym}.')
else:
    print("I'm Sorry,that word is not currently in the thesaurus.")

choice = input('\nWould you like to see the whole thesaurus (yes/no): ').lower().strip()
if choice == 'yes':
    for key, values in thesaurus.items():
        print(f'\n{key.title()} synonyms are:')
        for value in values:
            print(f'\t-{value}')
else:
    print('I hope you enjoyed the program. Thank you!')