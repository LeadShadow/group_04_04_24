# рядки
print('didn\'t')  # didn't
print("didn't")  # didn't

s = 'Hello world!'
# [5, 2, 10, 8, 4, 1, 3]
print(s[0])
print(s[-1])

# s = 'Hello world!'
# s[0] = 'Q'

# методи рядків
# .upper() -> повертає рядок де всі елементи в верхньому регістрі
s = 'Hello!'
s = s.upper()
print(s)


# .lower() -> повертає рядок де всі елементи в нижньому регістрі
s = 'HEllo!'
s = s.lower()
print(s)

# .startswith(some_str) -> перевіряє що рядок починається з підрядка some_str
s = 'Bill Jones'
print(s.startswith('Bi'))

number = '+380937316049'
if number.startswith('+380'):
    print('Цей номер український')


s = 'hello.png'
if s.endswith('.png'):
    print('це фотка')

# загальні операції для колекцій
# 1 - перевірка на входження in
a = '123141'
if '2' in a:
    print(f'2 in {a}')

# 2 к-сть елементів
a = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6, 11, 12, 19, 21, 7, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10, 3, 4, 5, 6, 7, 8, 9, 10}
counter = 0
for i in a:
    counter += 1

print(counter)
print(len(a))
