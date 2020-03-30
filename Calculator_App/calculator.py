def add(a, b):
    """Add two numbers and returns the sum"""
    summation = round(a + b, 4)
    print(f'The sum of {a} + {b} is {summation}')
    return f"{a} + {b} = {summation}"


def subtract(a, b):
    """Subtract two numbers and returns the difference"""
    difference = round(a - b, 4)
    print(f'The difference of {a} - {b} is {difference}')
    return f"{a} - {b} = {difference}"


def multiply(a, b):
    """Multiply two numbers and returns the product"""
    product = round(a * b, 4)
    print(f'The product of {a} * {b} is {product}')
    return f"{a} * {b} = {product}"


def division(a, b):
    """Divides two numbers and returns the quotient"""
    if b != 0:
        quotient = round(a / b, 4)
        print(f'The quotient of {a} / {b} is {quotient}')
        return f"{a} / {b} = {quotient}"
    else:
        print('You cannot divide by zero.')
        return 'DIV ERROR'


def exponent(a, b):
    """Take a number to a power and return the result"""
    power = round(a ** b, 4)
    print(f'The result of {a} raised to the {b} power is {power}')
    return f"{a} ** {b} = {power}"


def run_again():
    """User choice to run the program again"""
    choice = input('Would you like to run the program again [y/n]: ').lower()
    if choice != 'y':
        run = False
    else:
        run = True
    return run

# The main code
print('Welcome to the Calculator App')
print('Enter two numbers and an operation and the desired operation will be performed.')

history = []
running = True

while running:
    num_1 = float(input('\nEnter a number: '))
    num_2 = float(input('\nEnter a number: '))
    operator = input('Enter an Operation [Add]ition, [Sub]traction, [Mul]tiplication, [Div]ision, [Exp]onentiation: ').lower()

    # Call the appropriate function based on the value operator
    if operator == 'add':
        result = add(num_1, num_2)
    elif operator == 'sub':
        result = subtract(num_1, num_2)
    elif operator == 'mul':
        result = multiply(num_1, num_2)
    elif operator == 'div':
        result = division(num_1, num_2)
    elif operator == 'exp':
        result = exponent(num_1, num_2)
    else:
        print('That operation is not available.Try again')
        result = 'OPERATION ERROR'

    # Append the mathematical result to history
    history.append(result)
    # Allow user to quit
    running = run_again()
    if not running:
        print("\nCalculation Summary: ")
        for calc in history:
            print(calc)
        print("\nThank you for using the Python Calculator App. Goodbye.")

