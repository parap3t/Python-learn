# random_numbers = {1, 2, 3, 4, 5, 6}

# random_numbers2 = random_numbers

# random_numbers.add(10)

# #random_numbers.remove(15)

# random_numbers.discard(25)

# print(random_numbers)


# ages = set()

# elements_count = int(input("Введите количество элементов: "))

# for num in range(elements_count):

#     pupil_age = int(input("Введите возраст школьника: "))
    
#     ages.add(pupil_age)
  
# print(ages)


# names = {"Данил", "Егор", "Алексей"}

# elements_count = int(input("Введите количество элементов: "))

# for num in range(elements_count):

#     pupil_name = input("Введите имя школьника: ")
    
#     names.discard(pupil_name)
  
# print(names)

RANDOM_NUMBERS1 = {1, 5}
RANDOM_NUMBERS2 = {5, 1, 9, 10}

NUMBERS_UNION = RANDOM_NUMBERS1.union(RANDOM_NUMBERS2)
# NUMBERS_UNION = RANDOM_NUMBERS1 | RANDOM_NUMBERS2

NUMBERS_INTER = RANDOM_NUMBERS2.intersection(RANDOM_NUMBERS1)
# NUMBERS_INTER = RANDOM_NUMBERS2 & RANDOM_NUMBERS1

NUMBERS_DIFF = RANDOM_NUMBERS1.difference(RANDOM_NUMBERS2)
# NUMBERS_INTER = RANDOM_NUMBERS2 - RANDOM_NUMBERS1

NUMBERS_ISSUBSET = RANDOM_NUMBERS1.issubset(RANDOM_NUMBERS2)

NUMBERS_ISSUPERSET = RANDOM_NUMBERS2.issuperset(RANDOM_NUMBERS1)

print(NUMBERS_ISSUPERSET)