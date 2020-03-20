

print('Welcome to Database Admin Program.')

log_on_information = {
    'mooman74':'alskes145',
    'meramo1986':'kehns010101',
    'nickyD':'world1star',
    'george2':'booo3oha',
    'admin00':'admin1234',
    }

user_name = input('Enter your username:')

if user_name in log_on_information.keys():
    password = input('Enter your password: ')
    if password == log_on_information[user_name]:
        print(f'Hello,{user_name}!You are logged in.')
        if user_name == 'admin00':
            print('Here is the current user database:')
            for key, value in log_on_information.items():
                print(f'Username:{key}\t\tPassword:{value}')
        else:
            password_change = input('Would you like to change your password(yes/no):').lower().strip()
            if password_change == 'yes':
                new_password = input('Enter your new password(Password must be 8 characters long): ')
                if len(new_password) >= 8:
                    log_on_information[user_name] = new_password
                else:
                    print('Password not 8 characters long,try again.')
                print(f'{user_name} your password has been updated to {new_password}.')
            else:
                print(f'Goodbye {user_name}!!')
    else:
        print(f'{user_name} password is incorrect.')
else:
    print('Username is not in the database.')
