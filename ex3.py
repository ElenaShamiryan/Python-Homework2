def new_list(N):
    lst = []
    i = 0
    sum = 0
    for n in range(1, N+1):
        lst.append((1 + (1 / n))**n)
        sum = sum + lst[i]
        i = i + 1
    return sum


n = new_list(int(input('Введите число: ')))
print(round(n, 3))
