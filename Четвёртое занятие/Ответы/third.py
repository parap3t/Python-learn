user_num1 = float(input("Введите первое число: "))
user_num2 = float(input("Введите второе число: "))

if user_num1 == 0 or user_num2 == 0:
    print("На ноль делить нельзя!")
    
else:
    print(user_num1 / user_num2)