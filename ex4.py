N = int(input('Введите число: '))
list = []

for n in range(-N, N+1):
    list.append(n)
print(list)

a = int(input('Введите позицию первого эллемента: '))
b = int(input('Введите позицию второго эллемента: '))
length = int(N*2 + 1)
if 0 < a <= length and 0 < b <= length:
    mult = list[a]*list[b]
    print(f'Произведение элементов на данных позициях равно {mult}')
