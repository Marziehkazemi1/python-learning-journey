my_list = [2, 4, 5, 10]

doubled_numbers = list(map(lambda x: x * 2, my_list))
print(doubled_numbers)

numbers = [1, 4, 6, 5, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)