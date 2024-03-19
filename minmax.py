def minmax(numbers):
    if not numbers:
        return None

    smallest = largest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num
        elif num > largest:
            largest = num

    return smallest, largest

user_input = input("Enter numbers separated by space: ")
tup_numbers = [int(num) for num in user_input.split()]
result = minmax(tup_numbers)
print("Smallest and Largest numbers:", result)