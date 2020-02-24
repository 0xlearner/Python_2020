# Temperature Conversion App

print("Welcome to the Temperature Conversion App")

# Gather user input in fahrenheit
temp_f = float(input("\nWhat is the given temperature in Fahrenheit: "))

#Convert temps into celsius and kelvin
temp_c = (5/9)*(temp_f - 32)
temp_k = temp_c + 273.15

#Round temps
temp_f = round(temp_f, 4)
temp_c = round(temp_c, 4)
temp_k = round(temp_k, 4)

#Summary Table
print("\nDegrees Fahrenheit:\t" + str(temp_f))
print("Degrees Celsius:\t" + str(temp_c))
print("Degrees Kelvin:\t\t" + str(temp_k))