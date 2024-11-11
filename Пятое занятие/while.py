# Цикл while

# Бесконечный цикл, ибо условие никогда не станет ложным
while 2 > 0:
  print("2 > 0")
  
number = 1

while number < 10:
  
  print(number, end = " ") #-> 1 2 3 4 5 6 7 8 9 10
  
  number += 1


# number = 1

while number < 10:
  
    if number % 2 == 0:
      print("Число чётное:", number) # -> Число чётное: 2 и т.д
      
    number += 1
