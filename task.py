# # Запрашиваем данные
# integer = int(input('Введите целое число: '))
# decimal = float(input('Введите дробное число: '))
# string = input('Введите строку: ')

# # Вывод типов данных
# print(f"Значение: {integer}, тип: {type(integer).__name__}") 
# print(f"Значение: {decimal}, тип: {type(decimal).__name__}") 
# print(f"Значение: {string}, тип: {type(string).__name__}") 

a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

print(f"Сумма: {a + b}")
print(f"Разность: {a - b}")
print(f"Произведение: {a * b}")
print(f"Деление: {a / b}")
print(f"Целочисленное деление: {a // b}")
print(f"Остаток: {a % b}")
print(f"Степень: {a ** b:.2f}") 
# .2f спецификатор, который округляет до 2 знаков после запятой
