name = input("Як тебе звати? ")
age = int(input ("Скільки тобі років? "))
print(f"Привіт, {name}")
print(f"Тобі {age} років")
future_age = age + 5
print(f"Через 5 років тобі буде {future_age}")
if age >= 18:
    print("Ти повнолітній")
else:
    print("Ти ще молодий 😉")