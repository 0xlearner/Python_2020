print('Welcome to the Shipping Program')
#Define our list of users and Get user input
user = ['eramom', 'footea', 'davisv', 'papiknut', 'allenj']
username = input('\nHello,What is your username > ').lower().strip()

#Our user is in our list....
if username in user:
    print(f'\nHello {username},Welcome back to your Account.')
    print(f'Current Shipping prices are as follows:')
    print(f'\nShipping Orders 0 to 100: \t$5.10 each')
    print(f'Shipping Orders 100 to 500: \t$5.00 each')
    print(f'Shipping Orders 500 to 1000: \t$4.95 each')
    print(f'Shipping Orders over 1000: \t$4.80 each')

    # Determine price based on how many items are shipped
    quantity = int(input('How many items you would like to ship > '))
    if quantity <= 100:
        cost = 5.10
    elif quantity <= 500:
        cost = 5.00
    elif quantity <= 1000:
        cost = 4.95
    else:
        cost = 4.80

    # Display final cost
    bill = quantity * cost
    bill = round(bill,2)
    print(f'To ship {quantity} items it will cost you ${bill} at ${cost} per item.')

    # Place the order if the user desires
    choice = input('\nWould you like to place the order now (y/n) > ').lower()
    if choice.startswith('y'):
        print(f"Okay Shipping your {quantity} items.")
    else:
        print('No order is being placed at this time.')

#Our user is not in the list
else:
    print(f'Sorry,{username} you do not have account with us yet!')