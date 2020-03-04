import datetime

# Create the datetime object and store the current date and time
time_now = datetime.datetime.now()

# Welcome message
print('-' * 35)
print('Welcome to the Grocery Shopping App'.center(35))
print('-' * 35)
foods = ['Meat', 'Cheese']
print(time_now.strftime("%Y-%b-%d %H:%M"))
print(f'\nYou Currently have {foods[0]} and {foods[1]} in your list.')

# Get user input
while True:
    add_item = input('Add food to your grocery list (press "q" to end): ')
    if add_item == 'q':
        break
    add_item = foods.append(add_item.title())
    add_item = foods.sort()
print(f'Here is your updated list: {foods}')

#Simulate Shopping
for buy_items in foods:
    print(f'Current Grocery items: {len(foods)}')
    buy_items = input('What food did you just buy? ').title()
    if buy_items in foods:
        foods.remove(buy_items)
        print(f'Current Grocery List: {foods}')
print(f'Update List: {foods}')

#The store is out of an item...
no_item = foods.pop()
print(f'Sorry, the store is out of {no_item} at the moment.')
new_food = input('What food would you like instead: ').title()
foods.insert(0, new_food)
print(f'Here is what remains on your grocery list: \n{foods}')