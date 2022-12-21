print("How many seconds in a year")
print("--------------------------")
print()
# Ask user a yes or no question
isLeapOrNot = input("Is this year a leap year?\n> ").lower()

print()

# Set times 
days = 365
leapYear = 366
hours = 24
minutes = 60
seconds = 60

# Maths
# Is not a leap year calculation
answerYear = days * hours * minutes * seconds
# Is a leap year calculations
answerLeapYear = leapYear * hours * minutes * seconds

# The results
if isLeapOrNot == "yes":
  print("Number of seconds in a leap year are", answerLeapYear) # Result should be 31622400
elif isLeapOrNot == "no":
  print("Number of seconds in a year are", answerYear) # Result should be 31536000
else: # If yes or no are not chosen
  print("Please enter yes or no.")
