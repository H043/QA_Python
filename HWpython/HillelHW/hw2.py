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

elif (
    (user_selection == "Камень" and random_item == "Ножницы")
    or (user_selection == "Ножницы" and random_item == "Бумага")
    or (user_selection == "Бумага" and random_item == "Камень")
):
    print("Выбор компьютера", random_item)
    print("Вы победили")
else:
    print("Выбор компьютера", random_item)
    print("Вы проиграли")
    print("Выбор компьютера", random_item)
    print("Вы победили")
elif user_selection == "Камень" and random_item == "Бумага":
    print("Выбор компьютера", random_item)
    print("Вы проиграли")
elif user_selection == "Ножницы" and random_item == "Бумага":
    print("Выбор компьютера", random_item)
    print("Вы победили!")
elif user_selection == "Ножницы" and random_item == "Камень":
    print("Выбор компьютера",random_item)
    print("Вы проиграли")
elif user_selection == "Бумага" and random_item == "Камень":
    print("Выбор компьютера", random_item)
    print("Вы победили")
elif user_selection == "Бумага" and random_item == "Ножницы":
    print("Выбор компьютера", random_item)
    print("Вы проиграли")