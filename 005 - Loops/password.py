import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# password = ""

# for a in range(0, nr_letters):
#     password += random.choice(letters)

# for b in range(0, nr_symbols):
#     password += random.choice(symbols)

# for c in range(0, nr_numbers):
#     password += random.choice(numbers)

# print(password)


password = []

for a in range(nr_letters):
    password.append(random.choice(letters))

for b in range(nr_symbols):
    password.append(random.choice(symbols))

for c in range(nr_numbers):
    password.append(random.choice(numbers))

random.shuffle(password)    # can't shuffle string

output = ""
for letter in password:
    output += letter

print(output)

# Elegent
# pw_letters = ''.join(random.choices(letters, k=nr_letters))
# pw_symbols = ''.join(random.choices(symbols, k=nr_symbols))
# pw_numbers = ''.join(random.choices(numbers, k=nr_numbers))
# easy_password = pw_letters + pw_symbols + pw_numbers
# total = nr_letters + nr_symbols + nr_numbers
# hard_password = ''.join(random.sample(easy_password, k=total))
# print("Your password is: " + hard_password)