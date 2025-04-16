import string
import secrets

# Define the length of the password
length = 24

# Define the character set for the password
characters = string.ascii_letters + string.digits + string.punctuation

# Create an empty string for the password
password = ""

# Loop through the length and add a random character from the character set
for i in range(length):
  password += secrets.choice(characters)

# Print the password
print(password)