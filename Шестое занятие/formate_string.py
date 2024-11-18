user_name = input("Введите ваше имя: ")
user_age = int(input("Введите ваш возраст: "))

print(f"Добрый день, {user_name}. Вам {user_age} лет!")

print("Добрый день, {}. Вам {} лет!".format(user_name, user_age))
