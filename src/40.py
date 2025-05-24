def calculate_factorial(n):
    if n == 0:
        return 1
    else:
        return n * calculate_factorial(n - 1)

n = 5
print("Factorial of", n, "is:", calculate_factorial(n))
