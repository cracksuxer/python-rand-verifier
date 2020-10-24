import random


random_list = list()
list_repeated_element = list()
numbers = 10000000
most_repeated_numbers = list()


for x in range(numbers):
    random_list.append(random.randint(0, 100))

random_list.sort()

for index in range(101):
    list_repeated_element.append(random_list.count(index))

for number, index in enumerate(list_repeated_element):
    rounded_number = round(((index/numbers)*100), 5)
    print(f'El numero {number} se repite {rounded_number}%')
    if rounded_number >= 0.996:
        most_repeated_numbers.append(number)

print(f'\nMost repeated numbers are:\n{most_repeated_numbers}')
