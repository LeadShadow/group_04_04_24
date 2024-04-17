# Коментарі


# Типи даних
# None -> порожнє значення
# Числа(цілі числа, дробові, комплексні)
# Boolean(True or False)
# Рядки

a = 10  # int
b = 20  # int
print(a + b)  # 30

x = 3.3
print(0.1 + 0.2 == 0.3)  # False  # 0.300000000000000000004

# None
r = None

if a <= b:
    r = 10
elif a > b:
    r = 20
else:
    r = 30

print(r)

print(a < b)  # True
print(a > b)  # True

age = 18
if age >= 18:
    print('You are adult already')

adult1 = age >= 18
print(adult1)


# Рядки
hello_string = 'Hello'
world_string = 'World!'
print(hello_string[0])
print(f'{hello_string} {world_string}')  # Hello World!
print(hello_string + ' ' + world_string)  # Hello World!
# print('didn't'')
print('didn\'t')
print("didn't", 'daw', 'dwadwa')

a = input('Enter something: ')  # -> str
print(type(a))  # '20'
b = '10'
x = input('Enter something: ')
print(a + x)  # a = '10', b = '20',  '1020'

# Приведення типів
a = int(input('Enter something: ')) # -> int  #
print(type(a))
x = int(input('Enter something: '))
print(a + x)

# int, str, bool, float
pi = float('3.14')
print(type(pi))

pi_str = str(3.14)
print(type(pi_str))


# True(1), False(0)
print(bool(1))
print(bool(0))

# True(все шо буде не пустим рядком), False(пустий рядок)
print(bool('dawdwa'))
print(bool(''))

# None -> порожнеча(False)
print(bool(None))
