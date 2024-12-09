numbers = [1, 2, 3, 4, 5, 6]
num2 = numbers[::-1]

sum_of_num = []

for i, v in enumerate(numbers):
    sum_of_num.append(v + num2[i])
    
print(sum_of_num)