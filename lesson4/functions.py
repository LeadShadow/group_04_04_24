def say_hello():
    print('Привіт світ!')


say_hello()

def print_max(a, b):
    if a > b:
        print(f'a == {a} - максимальне')
    elif a == b:
        print('a == b')
    else:
        print(f'b == {b} - максимальне')


print_max(15, 11)
print_max(15, 11)
print_max(15, 11)
print_max(15, 11)
print_max(15, 11)
print_max(15, 11)


def plus(a, b):
    c = a + b
    return c

result = plus(3, 5)
print(result)

def plus(a, b):
    return a + b

print(plus(3, 5))


x = 50
def func():
    x = 2
    print(f'Заміна глобального x на {x}')

func()
print(f'x все ще {x}')


x = 50
def func():
    global x
    x = 2
    print(f'Заміна глобального x на {x}')

func()
print(f'значення x вже: {x}')

x = 50
def func():
    x = 2
    print(f'Заміна глобального x на {x}')
    return x

x = func() # -> x = 2
print(f'значення x вже: {x}')


def func(a, b=5, c=10):
    print(f'a == {a}, b == {b}, c == {c}')


func(3)
func(3, 6, 12)
func(a=10, c=25, b=30)

