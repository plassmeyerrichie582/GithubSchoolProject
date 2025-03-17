import random

def get_random_string(length):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    result = ''
    for i in range(length):
        result += random.choice(letters)
    return result