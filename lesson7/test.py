# методи списків

# remove(item) - метод remove видаляє елемент - де item це і є елемент
chars = ['a', 'b']
something = chars.remove('b')
print(chars)
print(something)

# pop(index) - метод pop видаляє елемент по індексу і повертає його
chars = ['a', 'b']
something = chars.pop(1)
print(chars)
print(something)

# extend(list) - це метод який розширює список іншим списком
chars = ['a', 'b']
numbers = [1, 2]
chars.extend(numbers)
print(chars)


# insert(i, x) - вставляє x на позицію з індексом i
chars = ['a', 'b']
chars.insert(1, 'x')
print(chars)

# index(item) - визначає індекс конкретного елементу
chars = ['a', 'b', 'c', 'd']
c_index = chars.index('c')
print(c_index)

# count(item) - к-сть елементів item всередині списку
chars = ['a', 'a', 'b', 'c', 'a']
a_count = chars.count('a')
print(a_count)


# sort() - метод сорт, сортує список
# у метода сорт, є атрибут reverse
numbers = [1, 10, 4, 8, 1328, -10, -25]
numbers.sort()
print(numbers)

numbers = [1, 10, 4, 8, 1328, -10, -25]
numbers.sort(reverse=True)
print(numbers)


# reverse() - повертає список в зворотньому порядку
numbers = [1, 10, 4, 8, 1328, -10, -25]
numbers.sort()
numbers.reverse()
print(numbers)


# copy() - копіює об'єкт
chars = ['a', 'b']
chars_copy = chars
print(chars_copy)
print(chars)
chars.append('c')
print(chars)
print(chars_copy)

chars_copy_ = chars.copy()
print(chars_copy_)
chars.append('d')
print(chars)
print(chars_copy_)

# словники

# pop(key) - видаляє пару ключ - значення і повертає значення ключа
chars = {'a': 1, 'b': 2}
b_num = chars.pop('b')
print(b_num)

# update(another_dict) - метод update, розширює словник, елементами іншого словника
chars = {'a': 1, 'b': 2}
chars.update({'c': 3})
print(chars)

# clear() - очищує словник

# copy() - створює копію

# get(key, default) - дістати і подивитись на значення ключа
chars = {'a': 1, 'b': 2}
b_index = chars.get('c', 0)
print(b_index)
# print(chars['c'])

numbers = {
    1: 'one',
    2: 'two',
    3: 'three'
}
print('-----------------------------------------------------------------------------')
for key in numbers:
    print(key)

print('-----------------------------------------------------------------------------')
for key in numbers.keys():
    print(key)


print('-----------------------------------------------------------------------------')
for value in numbers.values():
    print(value)


print('-----------------------------------------------------------------------------')
for key, value in numbers.items():
    print(key, value)


# множини
set_1 = {1, 1, 1, 2, 3, 3, 3}
print(set_1)

a = set()
print(a)

# add(item) - добавляє елемент в множину


# remove(element) - видаляє елемент з множини, викликає виняток, якшо такого елементу не існує в множині


# discard(element) - видаляє елемент з множини, не викликає виняток, якшо такого елементу не існує в множині


a = set('hello')

b = set('hi there!')

print(a)
print(b)


print(a & b)  # & -> and
