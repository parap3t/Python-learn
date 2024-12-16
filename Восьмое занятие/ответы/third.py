countries = {
              "Russia": {"people": 144_000_000},
              "USA": {"people": 334_998_398}
            }

user_country = input("Введите название страны на англ: ")

if countries.get(user_country) != None:
    del countries[user_country] # можно через pop
    print("Удаление успешно!", countries)
        
else:
    print("Такой страны нет в словаре!")
        
