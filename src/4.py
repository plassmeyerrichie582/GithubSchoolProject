import random

def get_random_code():
    """Returns a random 4-digit code"""
    return str(random.randint(1000, 9999)).zfill(4)
