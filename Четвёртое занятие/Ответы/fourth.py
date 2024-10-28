time_of_day = int(input("Введите время суток: "))

if 5 <= time_of_day < 12:
    print("Утро!")
    
elif 12 <= time_of_day < 19:
    print("Вечер!")
    
else:
    print("Ночь!")