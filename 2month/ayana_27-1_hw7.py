from random import randint, choice

p = []
for i in range(15):
    p.append(randint(0, 50))
print(f'unsorted list: {p}')


def buble_sort(a: list):
    for i in range(len(a) - 1):
        for j in range(len(a) - i - 1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    return a


value = choice(buble_sort(p))
print(f'desired number: {value}')
print(f'sorted list: {p}')


def bynary_search(item: int, ls: list):
    low = 0
    high = len(ls) - 1

    while True:
        if low < high:
            middle = (low + high) // 2
            if item == ls[middle]:
                low = middle
                high = low
                pos = middle
                print(f'Element is present at index: {pos}')
                break
            elif item > ls[middle]:
                low = middle + 1
            elif item < ls[middle]:
                high = middle - 1
        else:
            print('Element not found')
            break


bynary_search(value, p)
