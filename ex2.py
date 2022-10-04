def mult_numb(N):
    b = 1
    for i in range(1, N + 1):
        b = b*i
        print(b, end=' ')


a = int(input('Введите число: '))
mult_numb(a)
