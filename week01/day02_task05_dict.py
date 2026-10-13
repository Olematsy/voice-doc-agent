ages = {
    "Аня": 25,
    "Борис": 30,
    "Вика": 22,
}

name = input("Введи имя: ")

if name in ages:
    print(f"{name}: {ages[name]} лет")
else:
    print(f"{name} не найден")