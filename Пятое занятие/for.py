user_name = input("Введите своё имя: ")

for letter in user_name:
    print(letter, end = " ") #-> Ввод: Данил Вывод: Д а н и л


for num in range(1, 10, 1):
  print(num, end=" ") #-> 1 2 3 4 5 6 7 8 9

for num in range(5, 1, -1):
    print(num, end = " ") #5 4 3 2 