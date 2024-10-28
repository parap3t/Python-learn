# Условная конструкция else
name = input("Введите своё имя: ")

if name == "Alexandr":
    print("Вы Александр!")
  
elif name == "Danil":
    print("Вы Данил!")

else:
    print("Я вас не знаю!")    
    
number = int(input("Введите число :"))

if number > 0:
    print("Число положительное!")

elif number < 0:
    print("Число отрицательное!")
    
else:
    print("Число равно 0")