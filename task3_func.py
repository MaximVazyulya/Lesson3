def my_func(a,b,c):
	c = (a + b + c) - min(a,b,c)
	return c
a = float((input("Введите значение a = ")))
b = float((input("Введите значение b = ")))
c = float((input("Введите значение c = ")))
print("Сумма наибольших двух аргументов = ", my_func(a,b,c))