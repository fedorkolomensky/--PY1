import random

def get_unique_list_numbers() -> list[int]:
    list = []
    while(len(list)<15):
        n = random.randint(-10,10)
        if n not in list:
            list.append(n)
    return list

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))

#Второй способ:

def get_unique_list_numbers() -> list[int]:
    return random.sample(range(-10, 10), 15)

list_unique_numbers = get_unique_list_numbers()
print(list_unique_numbers)
print(len(list_unique_numbers) == len(set(list_unique_numbers)))