import random

N = int(input('Введите количество элементов в списке: '))
list = []


def first_list(list):
    for i in range(N):
        num = random.randint(-10, 10)
        list.append(num)
    print(f'Исходный  список: {list}')


first_list(list)
random.shuffle(list)
print(f'Рандомный список: {list}')
