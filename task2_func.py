def user_data(name, sername, year, town, email, phone):
	my_dict = {"Имя: ": name, "Фамилия : ": sername, "Город рождения: ": town, "Почта : ": email, "Телефон : ": phone}
	print(my_dict)

n = input("Введите имя :")
s = input("Введите фамилию :")
y = input("Введите год рождения :")
t = input("Введите город рождения :")
e = input("Введите эл. почту :")
p = input("Введите телефон :")

user_data(name=n,sername=s,year=y,town=t,email=e,phone=p)