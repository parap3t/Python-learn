DICT1 =  {"a": 100, "b": 200, "c": 300}
DICT2 = {"b": 250, "d": 400}

dict_union = DICT1.copy()

for key, value in DICT2.items():
    
    value_of_dict2 = DICT1.get(key)
    EMPY = None
    
    if value_of_dict2 != EMPY:
        
        summary = value + value_of_dict2
        dict_union[key] = value + value_of_dict2
          
    else:
        dict_union[key] = value
        
print(dict_union)