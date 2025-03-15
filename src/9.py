import random

def get_random_code():
    code = ''
    for i in range(10):
        code += chr(random.randint(65, 90))
    return code

get_random_code()
