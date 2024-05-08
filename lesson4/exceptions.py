# винятки

# try, except

try:
    int('a')
except ValueError:
    print('Це значення неможливо перетворити на ціле число')

print('dawdaw')
print('dawdaw')
print('dawdaw')
print('dawdaw')


value = '10'

try:
    value = int(value)
except ValueError:  # TypeError
    print(f'value {value} is not a number')
else:
    print(value > 0)
finally:
    print('This will be printed anyway')


# чи можна обробити будь-яку помилку, яка виникає в блоці try?

# ValueError - виникає коли тип операнда підходить, але значення таке шо операцію виконати неможливо
# SyntaxError
# ZeroDivisionError - ділення на нуль
# TabError