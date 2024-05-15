def say(message, times=1):
    print(message * times)


say('Привіт')
say(message='Привіт', times=5)


def total(a=5, *numbers, **phone_book):
    print(f'a == {a}')

    for item in numbers:  # (1, 2, 3, 4, 5)
        print(f'item == {item}')

    for key, value in phone_book.items():  # {'Sasha': '+380937316048', 'Misha': '+380937316048'}
        print(key, value)


total(10, 1, 2, 3, 4, 5, Sasha='+380937316048', Misha='+380937316048')

# кортежі
my_tuple = tuple()
another_tuple = ()
print(my_tuple, another_tuple)

not_empty = (1, 2, 3)
print(not_empty[0])
print(not_empty[1])
print(not_empty[2])
# print(not_empty[3])


# словник
empty_dict = {}
another_empty_dict = dict()
print(empty_dict, another_empty_dict)

some_dict = {'key': 'value',
             1: 'one',
             2: 'two'
             }
print(some_dict)

not_empty = {'key': 'value'}
if not_empty:
    not_empty['new_key'] = 'new_value'

print(not_empty)


# рекурсія

# 5! -> 5 * 4! -> 5 * 4 * 3! -> 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)  # 5 * factorial(4), factorial(4) -> 4 * factorial(3), factorial(3) -> 3 * factorial(2) -> 2 * factorial(1)

print(factorial(5))

n = 5
count = 1
while n > 1:
    count = count * n
    n = n - 1

print(count)