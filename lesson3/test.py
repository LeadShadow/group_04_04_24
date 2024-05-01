# тернарні операції
# блоки інструкцій
# цикли
# винятки

# тернарні операції
is_nice = True
state = 'nice' if is_nice else 'not nice'

some_data = None  # False
msg = some_data or 'Не було повернено даних'  # False or True -> True

if is_nice:
    state = 'nice'
else:
    state = 'not nice'

# блоки інструкцій
x = int(input('x: '))
y = int(input('y: '))

if x == 0:
    print("x can't be equal to zero")
    x = int(input('x: '))
    if x == 0:
        print("x can't be equal to zero")
        x = int(input('x: '))
        if x == 0:
            print("x can't be equal to zero")
            x = int(input('x: '))
            if x == 0:
                print("x can't be equal to zero")
                x = int(input('x: '))
                if x == 0:
                    print("x can't be equal to zero")
                    x = int(input('x: '))
                    if x == 0:
                        print("x can't be equal to zero")
                        x = int(input('x: '))
                        if x == 0:
                            print("x can't be equal to zero")
                            x = int(input('x: '))
                            if x == 0:
                                print("x can't be equal to zero")
                                x = int(input('x: '))

result = y / x


if x >= 0:
    if y >= 0:
        print('Перша чверть')
    else:
        print('Четверта чверть')
else:
    if y >= 0:
        print('Друга чверть')
    else:
        print('Третя чверть')

# x=10, y=10
