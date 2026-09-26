c = float(input("Введите третье число: "))
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
# Принимаем 3 числа
average = (a + b + c) / 3 # Вычисление ср. ариф.
minimum = min(a, b, c) # Нахождение минимума
maximum = max(a, b, c) # Нахождение максимума

print(f"Среднее арифметическое: {average:.2f}")
print(f"Минимум: {minimum}")
print(f"Максимум: {maximum}")
