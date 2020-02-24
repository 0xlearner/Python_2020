# Letter_Count_App

print("Welcome to the Letter Counter App")
# Get user input
user_name = input("\nWhat is your name: ").title().strip()
print("Hello, " + user_name + "!")

print("I will count the number of times that a specific letter occurs in a message.")

message = input("\nPlease enter a message: ")
letter = input('\nWhich letter would you like to count the occurences of: ')

# Standardize to lower case
message = message.lower()
letter = letter.lower()

# Get the count and display results
letter_count = message.count(letter)
print("\n" + user_name + ", your message has " + str(letter_count) + " " + letter + "'s in it.")
