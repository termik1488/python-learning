def get_numbers(): 
    numbers = []
    while True:
        number = int(input("введи число (0 щоб завершити) :")) 
        if number == 0: 
            break 
        numbers.append(number) 
    return numbers
def calculate_stats(numbers):
    if not numbers:
        return 0, 0
    total = sum(numbers)
    average = total / len(numbers)
    return total, average
numbers = get_numbers()
total, average = calculate_stats(numbers)
print(numbers)
print(total,average)