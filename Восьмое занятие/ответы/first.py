N = int(input("Введите число n: "))

nums_squares = {}

for number in range(1, N+1):
    
    square_num = number ** 2
    nums_squares[number] = square_num
    
print(nums_squares)