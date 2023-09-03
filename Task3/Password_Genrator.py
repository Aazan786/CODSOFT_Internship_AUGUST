import random
import string

class PasswordGenerator:
    def __init__(self):
        self.length = 12  # Default password length

    def set_length(self, length):
        self.length = length

    def generate_password(self, complexity_level):
        lowercase_letters = string.ascii_lowercase
        uppercase_letters = string.ascii_uppercase
        digits = string.digits
        special_characters = string.punctuation

        characters = lowercase_letters

        if complexity_level == 2:
            characters += uppercase_letters
        elif complexity_level == 3:
            characters += uppercase_letters + digits
        elif complexity_level == 4:
            characters += uppercase_letters + digits + special_characters

        if self.length < 4:
            print("Password length must be at least 4 characters.")
            return ""

        password = ''.join(random.choice(characters) for _ in range(self.length))
        return password

def main():
    password_generator = PasswordGenerator()

    try:
        length = int(input("Enter the desired password length: "))
        complexity_level = int(input("Select password complexity (1 for lowercase, 2 for lowercase and uppercase, 3 for all, 4 for all + special characters): "))

        password_generator.set_length(length)
        password = password_generator.generate_password(complexity_level)

        if password:
            print("Generated Password:", password)
    except ValueError:
        print("Invalid input. Please enter valid integers for password length and complexity level.")

if __name__ == "__main__":
    main()
