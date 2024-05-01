# цикли
# цикл for - перебір якоїсь послідовності
# цикл while - поки виконується якась умова тоді роби повторення

# ітерація - повторення якоїсь дії

fruit = 'apple'
for char in fruit:
    print(char)

print(char)

count_of_all_numbers = 0
# (1, 10) -> 1, 2, 3, 4, 5, 6, 7, 8, 9
for i in range(1, 10):
    count_of_all_numbers += i  # 2

print(count_of_all_numbers)

a = 1
while a <= 5:  # False
    print(a)
    a += 1


a = 0
while True:
    print(a)
    if a >= 20:
        break
    a += 1  # a = a + 1

while True:
    user_input = input('Input something: ')
    print(user_input)
    if user_input == 'exit':
        break

a = 0
while a < 6:
    a += 1
    if not a % 2:  # % - остача від ділення  a % 2 -> not 0(False) -> True  a % 2 -> not 1(True) -> False
        continue
    print(a)

