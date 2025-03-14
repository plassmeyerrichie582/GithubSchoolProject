import random

def get_random_number(low: int, high: int) -> int:
    """Generate a random number within a given range.

    Args:
        low (int): The lowest value of the range.
        high (int): The highest value of the range.

    Returns:
        int: A randomly generated number within the given range.
    """
    return random.randint(low, high)