import datetime

def print_header():
    print('-' * 30)
    print('Birthday Countdown'.center(30))
    print('-' * 30)
def get_user_birthday():
    print('When were you born?')
    year = int(input('Year [YYY]: '))
    month = int(input('Month [MM]: '))
    day = int(input('Day [DD]: '))

    birthday = datetime.datetime(year,month,day)
    return birthday
def compute_days_between_dates(original_date,target_date):
    this_year = datetime.date(target_date.year,original_date.month,original_date.day)
    dt = this_year - target_date
    return dt.days
def print_birthday_information(days):
    if days < 0:
        print(f"You had your birthday {-days} days ago this year.")
    elif days > 0:
        print(f"Your birthday is in {days} days!")
    else:
        print('Happy Birthday!!!')
def main():
    print_header()
    bday = get_user_birthday()
    today = datetime.date.today()
    number_of_days = compute_days_between_dates(bday,today)
    print_birthday_information(number_of_days)
main()