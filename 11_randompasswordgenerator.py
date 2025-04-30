import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choices(characters, k=length))
    return password

# Example usage
length = int(input("Enter password length: "))
print("🔐 Your secure password is:", generate_password(length))
