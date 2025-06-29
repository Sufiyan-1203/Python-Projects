import random
import string

def generate_password(length=12):
    if length < 8:
        return "Password must be at least 8 characters long"

    special_chars = '@&_-'
    lower = random.choice(string.ascii_lowercase)
    upper = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice(special_chars)

    allowed_chars = string.ascii_letters + string.digits + special_chars
    rest = random.choices(allowed_chars, k=length - 4)

    password = [lower, upper, digit, special] + rest
    random.shuffle(password)

    return ''.join(password)

length = int(input("Enter password length (minimum 8): "))
print("Generated Password:", generate_password(length))
