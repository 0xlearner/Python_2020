print('Welcome to the Voter Registration App')

#Get user input
user = input('\nPlease enter your name > ').title().strip()
age = int(input('Please enter your age > '))

#Define our parties List
parties = {1 : 'Republican', 2 : 'Democratic', 3 : 'Independent', 4 : 'Libertarian', 5 : 'Green'}

#If the user is above 18,they can vote
if age > 17:
    print(f'\nWelcome Aboard! {user},You can register to vote.')
    print('Here is the list of political parties you can vote for:')

    for i,party in enumerate(parties.values()):
        print(f'*Press{[i+1]} for {party}')

    #Print a message specific to the party chosen
    chosen = int(input('Which Party do you want to vote > '))
    if chosen in parties.keys():
        for key, value in parties.items():
            if key == chosen:
                print(f'Thank you {user},Your vote to {value} party has been casted.')
    else:
        print('Invalid input!')
else:
    print(f'Sorry,{user} you can not vote.You must be 18+ to cast a vote.')