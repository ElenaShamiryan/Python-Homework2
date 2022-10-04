def sum_of_digits(num):
    sum = 0
    for i in num:
        if i.isdigit():
            sum = sum + int(i)
    return sum


n = input('Введите число: ')
print(f'Сумма цирф в числе {n} равна {sum_of_digits(n)}')
