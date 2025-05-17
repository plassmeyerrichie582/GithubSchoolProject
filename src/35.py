def add_numbers(a: int, b: int) -> int:
    """
    This function adds two numbers and returns their sum.
    
    Parameters:
    a (int): The first number to be added.
    b (int): The second number to be added.
    
    Returns:
    int: The sum of the two numbers.
    """
    return a + b

def greet_user(name: str) -> None:
    """
    This function greets the user by their name and returns nothing.
    
    Parameters:
    name (str): The name to be greeted.
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    # Example usage
    result = add_numbers(5, 3)
    greet_user("Alice")
