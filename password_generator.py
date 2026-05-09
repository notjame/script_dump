import random

letters = ['a', 'b', 'c', 'e', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'E', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_of_lists = [letters, symbols, numbers]

def generate_password(length_of_password):
    password = ''
    for i in range(length_of_password + 1):
        char_choice = random.choice(list_of_lists)
        password += random.choice(char_choice)
    print(password)

generate_password(9)