"""
Найти медиану
Дано: массив чисел arr.
Найти: медиану массива. Оценить сложность алгоритма по затратам cpu, ram.
Условия: нельзя использовать сторонние библиотеки. Только чистый python.
"""
def median(arr):
    arr_sorted = sorted(arr)
    n = len(arr_sorted)
    if n % 2 == 1:
        return arr_sorted[n//2]
    else:
        return (arr_sorted[n//2 - 1] + arr_sorted[n//2]) / 2

