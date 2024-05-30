# імпорт пакетів і модулів
# import math  # імпортував пакет math

# sin_pi = math.sin(math.pi)
from math import sin, pi
from hello import say_hello
sin_pi = sin(pi)

say_hello('Sasha')

# точка входу

# колекції - структури даних
# словники
# кортежі
# списки
# множини

# впорядкованість
# незмінність
# змінність
# унікальність

# списки
my_list = []

empty_list = list()

print(my_list, empty_list)

not_empty = [1, 2, 3, 'Sasha']
print(not_empty)

some_iterable = ['a', 'b', 'c']
first_letter = some_iterable[0]
second_letter = some_iterable[1]
third_letter = some_iterable[2]
print(first_letter)
print(second_letter)
print(third_letter)
print(some_iterable)


some_iterable = ['a', 'b', 'c']
first_letter = some_iterable[-1]
second_letter = some_iterable[-2]
third_letter = some_iterable[-3]

print(first_letter)
print(second_letter)
print(third_letter)
print(some_iterable)

some_iterable[1] = 'x'
print(some_iterable)

# зрізи
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = numbers[0:5]
print(first_five)


odd_numbers = numbers[0:10:2]
even_numbers = numbers[1:10:2]
three_numbers = numbers[2:10:3]


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
first_five = numbers[0:5]
print(first_five)


odd_numbers = numbers[::2]
even_numbers = numbers[1::2]
three_numbers = numbers[2::3]


numbers_copy = numbers[:]  # numbers = Хрещатик 20
numbers.append(1)  # Хрещатик 20 -> Хрещатик 21

# Використання методів об'єктів

# append(item) - метод який добавляє елемент всередину списка(в кінець)
numbers = [1, 2, 3]
numbers.append(4)
print(numbers)

# clear() - метод який очищує вміст списку
nums = [1, 2, 3, 4]
nums.clear()
print(nums)