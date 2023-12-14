import random

user_selection = input("Введите Камень или Ножницы или Бумага: ")

choice = ["Камень", "Ножницы", "Бумага"]
if user_selection not in choice:
    print("Ви ввели неправильное значение")
    exit()
random_item = random.choice(choice)

if user_selection == random_item:
    print("Выбор компьютера", random_item)
    print("Ничья")

if user_selection == "Камень" and random_item == "Ножницы":
    print("Выбор компьютера", random_item)
    print("Вы победили")
if user_selection == "Камень" and random_item == "Бумага":
    print("Выбор компьютера", random_item)
    print("Вы проиграли")
if user_selection == "Ножницы" and random_item == "Бумага":
    print("Выбор компьютера", random_item)
    print("Вы победили!")
if user_selection == "Ножницы" and random_item == "Камень":
    print("Выбор компьютера",random_item)
    print("Вы проиграли")
if user_selection == "Бумага" and random_item == "Камень":
    print("Выбор компьютера", random_item)
    print("Вы победили")
if user_selection == "Бумага" and random_item == "Ножницы":
    print("Выбор компьютера", random_item)
    print("Вы проиграли")