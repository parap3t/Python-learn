FRUITS_COUNT = 3

fruits = []
fruits_amount = {}

for _ in range(FRUITS_COUNT):
    fruit_name = input("Введите название фрукта: ")
    fruits.append(fruit_name)
    
for i in range(FRUITS_COUNT):
    
    fruit_name = fruits[i]
    fruit_amount = int(input(f"Введите количество {fruit_name}: "))
    fruits_amount[fruit_name] = fruit_amount
    
print(fruits_amount)