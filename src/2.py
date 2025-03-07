import random

def generate_random_python_code():
    # Define a list of possible Python statements
    statements = ['print("Hello, world!")', 'x = 5', 'y = "hello"', 'if x > 3:', 'else:']
    
    # Generate a random index for the statement to use
    idx = random.randint(0, len(statements) - 1)
    
    # Return the selected statement
    return statements[idx]