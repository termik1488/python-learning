"""
Finds the second largest unique number from user input.
Handles edge cases (empty list, duplicates).
"""
def get_numbers(): 
    numbers = []
    while True:
        number = input("Введи число (Enter щоб завершити): ")
        if number == "": 
            break 
        try:
            number = int(number)
        except:
            print("Введи коректне число!")
            continue
        numbers.append(number) 
    return numbers
def find_second_max(numbers):
    if len(numbers)<2:
        return None
    max_value = max(numbers)
    second_max=None  
    for number in numbers:
        if number != max_value and (second_max is None or number > second_max):
            second_max = number
    return second_max        
numbers = get_numbers()
second = find_second_max(numbers)

if second is None:
    print("Другого унікального числа немає")
else:
    print("Друге найбільше:", second)
