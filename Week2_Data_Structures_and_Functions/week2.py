# Week 2: Data Structures and Functions

def remove_duplicates(data):
    return list(set(data))

def filter_even_numbers(data):
    return list(filter(lambda x: x % 2 == 0, data))

def sum_of_squares(data):
    return sum([x**2 for x in data])

def clean_data():
    data = input("Enter numbers separated by spaces: ").split()
    data = [int(x) for x in data]
    cleaned = remove_duplicates(data)
    print("Cleaned Data:", cleaned)

if __name__ == "__main__":
    numbers = [1, 2, 2, 3, 4, 4, 5]
    print("Even Numbers:", filter_even_numbers(numbers))
    print("Sum of Squares:", sum_of_squares(numbers))
    clean_data()
