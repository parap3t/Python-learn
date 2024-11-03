user_num = int(input("Введите положительное целое число: "))
sum_of_num = 0

for num in range(1, user_num + 1):
    sum_of_num += num
    
print("Сумма = ", sum_of_num)