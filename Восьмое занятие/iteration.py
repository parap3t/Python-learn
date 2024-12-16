# Перебор словаря

# для переора ключей словаря можно использовать следующую конструкцию

CITIES = {
    "Kurgan": 300_000,
    "Moscow": 1_000_000
}

for city in CITIES:
    print(city)
    
    
# Также можно выводить и занчение по ключу

for key in CITIES:
    print(key, CITIES[key])
    
# Но для большей читаемости рекоммендую писать так

for key in CITIES.keys():
    print(key, CITIES[key])
    
# Также можно перебрать и значения словаря

for value in CITIES.values():
    print(value)
    
# Существует возможность перебрать словарь по элементно

for element in CITIES.items():
    print(element)
