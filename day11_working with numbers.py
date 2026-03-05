def get_numbers():
    numbers = []
    while True:
        number = input("Введи число Enter щоб завершити")
        if number == "":
            break
        try:
            number = int(number)
        except:
            print("Введи коректне число!")
            continue
        numbers.append(number) 
    return numbers
numbers = get_numbers()
if not numbers:
    print("список порожній")
else:
    count = len(numbers)
    total = sum(numbers)
    average = total / count
    max_value = max(numbers)
    min_value = min(numbers)
    even_count = 0
    odd_count = 0
    larger_average = 0
    smaller_average = 0
    for number in numbers:
        if number % 2 == 0:
            even_count +=1
        else: 
           odd_count +=1
        if number > average:
            larger_average +=1
        elif number < average:
           smaller_average +=1   
def find_second_min(numbers):
    second_min = None
    for number in numbers: 
        if number > min_value and ( second_min is None or number < second_min):
            second_min = number
    return second_min
second_min = find_second_min(numbers)
if second_min is None:
    print   ("другого найменшого немає")
else:
    print("друге найменше число", second_min)
print("кількість чисел:", count)
print("сума чисел:", total)
print("Середнє значення:", average)
print("Найбільше число:", max_value)
print("найменьше число:", min_value)
print("кількість парних:", even_count)
print("кількість непарних:", odd_count)
print("більших за середнє:", larger_average)
print("менших за середнє:", smaller_average)