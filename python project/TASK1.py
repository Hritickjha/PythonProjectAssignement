import random

# Define the word lists
list1 = ['hari', 'deepak', 'suraj', 'sanju', 'gaurav', 'krishna', 'raju']
list2 = ['white', 'red', 'pink', 'red', 'sky blue']
list3 = ['donkey', 'monkey', 'elephant', 'cat']


# Prompt the user for the number of passwords needed
print("Password Generator")
print("==================")
print()
num_passwords = int(input("How many passwords are needed?: "))

# Check if the number is within the allowed range
if num_passwords < 1 or num_passwords > 24:
  print("Please enter a value between 1 and 24.")
else:
  # Generate the passwords
  for i in range(1, num_passwords + 1):
    password = random.choice(list1) + random.choice(list2) + random.choice(list3) 
    print("  ", i, "-->", password)
  