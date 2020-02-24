# Miles per hour to Meter per second Conversion App

print("Welcome to the MPH to MPS Conversion App")

#Get the user input
mph = float(input("\nWhat is your speed in miles per hour: "))

#Convert to meter per second
mps = mph*0.4474
mps = round(mps, 2)

print("Your speed in meter per second is " + str(mps) + ".")
