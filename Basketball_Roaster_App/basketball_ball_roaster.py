
print('-' * 40)
print('Welcome to the Basketball Roster Program'.center(40))
print('-' * 40)

# Get user input and define our roster
roaster = {}
while True:
    players = input('players: ')
    positions = input('positions: ')
    roaster[players] = positions
    if len(roaster) == 5:
        break
print(roaster)
# Display roster
print(f'\t\tYour starting {len(roaster)} for the basketball season.')
for keys,values in roaster.items():
    print(f'\t\t{str(keys).replace("[","").replace("]","").title()}: \t\t {str(values).replace("[","").replace("]","").title()}')

# Remove an injured player
injured_player = roaster.popitem()
injured_player = str(injured_player)
print("""Oh no! {} is injured""".format(injured_player).replace("(","").replace(")","").replace("'","").title())
print(f'Your roaster only has {len(roaster)} players')

# Add a new player
new_player = input('Who will take the new spot: ').title()
new_player = roaster.setdefault(new_player,"center")
print(f'\t\tYour starting {len(roaster)} for the basketball season.')
for keys,values in roaster.items():
    print(f'\t\t{str(keys).replace("[","").replace("]","").title()}: \t\t {str(values).replace("[","").replace("]","").title()}')
# print(roaster)
