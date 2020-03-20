print("Welcome to the Yes or No Issue Polling App")

issue = input('What is the yes or no issue you will be voting on today: ')
vote_number = int(input('Number of voters you will allow on this issue: '))
pwd = input('Enter password: ')

yes = 0
no = 0
results = {}

for i in range(vote_number):
    name = input('Enter your name: ').title().strip()
    if name in results.keys():
        print('Sorry,it seems that someone with that name has already voted.')
    else:
        print(f'Here is our issue:{issue}')
        choice = input('What dou you think ...yes or no: ').lower().strip()
        if choice == 'yes' or choice == 'y':
            choice = 'yes'
            yes += 1
        elif choice == 'no' or choice == 'n':
            choice = 'no'
            no += 1
        else:
            print("That is not a yes or no answer, but okay...")

        results[name] = choice
        print(f'Thank you {name}!Your vote of {results[name]} has been recorded.')

total_voters = len(results.keys())
print(f'The following {total_voters} people voted on the issue {issue}')
for key in results.keys():
    print(f'-{key}')

print(f'\nOn the following issue:{issue}')
if yes > no:
    print(f'Yes wins! {yes} votes to {no}.')
elif no > yes:
    print(f'No wins! {no} votes to {yes}.')
else:
    print(f'It was a tie! {no} votes to {yes}')


admin = input('To see the voting results enter the admin password: ')
if admin == pwd:
    for key, value in results.items():
        print(f'Name:{key}\t\t\tVote:{value}')
else:
    print('Sorry,that is not the correct password.')
print('Thank you for using the Yes or No issue app.')