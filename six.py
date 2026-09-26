print("Конвертер температур")
print("1. Из Цельсия в Фаренгейт")
print("2. Из Фаренгейт в Цельсия")

choice = input("(1/2): ")

match choice:
    case '1':
        celsius = float(input("Введите температуру в °C: "))
        far = celsius * 9/5 + 32
        print(f"{celsius:.1f}°C = {far:.1f}°F")
    case "2":
        far = float(input("Введите температуру в °F: "))
        celsius = (far - 32) * 5/9
        print(f"{far:.1f}°F = {celsius:.1f}°C")
    case _:
        print("Такого выбора нет")
        

