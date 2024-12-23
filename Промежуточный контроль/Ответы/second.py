user_string = input("Введите строку: ")

print(f"""Длина строки = {len(user_string)}
Количество пробелов в строке = {user_string.count(" ")}
Первая и последняя буквы строки {user_string[0]}, {user_string[len(user_string) - 1]}
Строка в верхнем и нижнем регистре {user_string.lower()}, {user_string.upper()}
            """)