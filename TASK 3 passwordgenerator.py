import random
import string

length = int(input("Enter password length: "))

all_characters = string.ascii_letters+string.digits+string.punctuation

password = ''.join(random.choice(all_characters) for i in range(length))

print("generated password:",password)
