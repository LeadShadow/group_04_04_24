# умови - умовне виконання коду, тобто виконання блоку інструкцій якшо виконується певна умова
# цикли - повторення виконання блоку інструкцій поки виконується якась умова
# винятки - виконання блоку інструкцій в випадку помилки
age = int(input('How old are you?: '))

if age >= 18:  # age >= 18 -> True
    print('You are adult already')
else:
    print('You are infant yet')


a = int(input('Введіть число: '))
if a > 0:
    print('Число додатнє')
elif a < 0:
    print("Число від'ємне")
else:
    print('Це число нуль')


a = int(input('Введіть число: '))

if a == 1:
    print("Число == 1")
elif a > 0:
    print('Число додатнє і точно не 1')
else:
    print('Це число нуль або від\'ємне')


# логічні вирази
# 1 число 0 приводиться неявно до False
money = 0
if money:
    print(f'You have {money} on your bank account')
else:
    print('You have no money')

# 2 None теж неявно приводиться до False
result = None
if result:
    print('Ура в нас є результат і нам підвищать зарплатню')
else:
    print('Погано! в нас немає підвищення')

# 3 пустий контейнер приводиться до False
user_name = input('Enter your name: ')  # user_name = 'Sasha', user_name = ''

if user_name:
    print(f'Hello {user_name}')
else:
    print('Hello Anonym!')


# and(I) -> * False(0) and(*) True(1) -> 0 * 1 -> 0(False)
print(True and True)  # True
print(False and True)  # False
print(True and False)  # False
print(False and False)  # False

# or(або) -> + True or True -> 1 + 1 -> 1(True)
# or(або) -> + False or True -> 0 + 1 -> 1(True)
print(True or True)  # True
print(False or True)  # True
print(True or False)  # True
print(False or False)  # False

# not
print(not True)  # False
print(not False)  # True