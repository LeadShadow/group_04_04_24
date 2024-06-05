# У нас є список показань заборгованостей з комунальних послуг наприкінці місяця.
# Заборгованості можуть бути від'ємними — у нас переплата, чи додатними, якщо необхідно
# сплатити за рахунками. Напишіть функцію amount_payment, яка приймає на вхід список платежів,
# підсумовує додатні значення та повертає суму платежу наприкінці місяця.
# [100, -200, 150, 300, -350]
def amount_payment(payment):
    sum_ = 0
    for i in payment:
        if i > 0:
            sum_ += i
    return sum_


print(amount_payment([100, -200, 150, 300, -350]))