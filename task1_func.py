print("Программа вычисления результата от деления чисел a/b")
def div_ab(a, b):
	d = a/b
	return d

a = float(input("Введите число a : "))
b = float(input("Введите число b : "))
try:
    x = div_ab(a, b)
	print(f"Результат a/b = {x:.2f}")
except ZeroDivisionError:
	print("Деление на ноль не выполняется")



