def calculate_average(numbers):
    total = sum(numbers)
    average = total / len(numbers)
    return average

numbers = [1.0, 2.0, 3.0, 4.0, 5.0]
average = calculate_average(numbers)
print("The average is:", average)
