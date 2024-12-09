numbers = [2, 1, 2, 3, 4, 5, 6]

for num in numbers:
    if numbers.count(num) > 1:
        numbers.remove(num) 
        
print(numbers)