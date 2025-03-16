import random

def get_random_number(n):
    return random.randint(1, n)

def main():
    print(get_random_number(10))

if __name__ == "__main__":
    main()
