numbers = [1, 2, 1, 2, 2, 5, 9, 19 ,203, 203]

max_repit = 0

for num in numbers:
    if numbers.count(num) > numbers.count(max_repit):
        max_repit = num

print(max_repit)
