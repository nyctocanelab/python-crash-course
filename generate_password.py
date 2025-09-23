UPPERCASE_ALPHABETS ={chr(i) for i in range(65, 91)}
LOWERCASE_ALPHABETS = {chr(i) for i in range(97, 123)}
DIGITS = {str(i) for i in range(10)}
SPECIAL_CHARACTERS = {'!', '@', '#', '$', '%', '^', '&', '*', 
                      '(', ')', '-', '_', '=', '+'}
ALL_CHARACTERS = (UPPERCASE_ALPHABETS | LOWERCASE_ALPHABETS | 
                  DIGITS | SPECIAL_CHARACTERS)
import random
import string

def generate_password(length=12):
    while True:
        length = input("Enter the desired password length (minimum 4): ")
        try:
            length = int(length)
        except ValueError:
            print("Password length should be an integer.")
            continue
        if length < 4:
            print("Password length should be at least 4 characters.")
            continue
        break

    password = [
        random.choice(list(UPPERCASE_ALPHABETS)),
        random.choice(list(LOWERCASE_ALPHABETS)),
        random.choice(list(DIGITS)),
        random.choice(list(SPECIAL_CHARACTERS))
    ]
    
    password += random.choices(list(ALL_CHARACTERS), k=length-4)
    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    print("Generated Password:", generate_password())