# Import the random module to generate random characters
import random

# Import the string module to get letters and numbers
import string

# Ask the user to enter the required password length
length = int(input("Enter password length: "))

# Create a collection containing uppercase letters,
# lowercase letters, and numbers
characters = string.ascii_letters + string.digits

# Generate a random password using the selected characters
password = ''.join(random.choice(characters) for _ in range(length))

# Display the generated password
print("Generated Password:", password)