"""
Дан упорядоченный массив arr и число X, нужно найти индекс максимального элемента arr,
не превосходящего X. Если такого элемента не существует, вернуть -1.
"""

def max_lower_or_equal(sorted_arr, value):
    # Сначала проверим, существует ли искомый элемент
    if not sorted_arr or sorted_arr[0] > value:
        return -1

    left_idx, right_idx = 0, len(sorted_arr)
    while left_idx + 1 < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_arr[mid_idx] <= value:
            left_idx = mid_idx
        else:
            right_idx = mid_idx
    return left_idx

# ЗАХОДИТ В БЕСКОНЕЧНЫЙ ЦИКЛ

def max_lower_or_equal2(sorted_arr, value):
    # Сначала проверим, существует ли искомый элемент
    if not sorted_arr or sorted_arr[0] > value:
        return -1

    left_idx, right_idx = 0, len(sorted_arr)
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if sorted_arr[mid_idx] <= value:
            left_idx = mid_idx
        else:
            right_idx = mid_idx
    return left_idx

arr = [1, 2, 4, 7, 9]
value = 6
result = max_lower_or_equal(arr, value)
print(result)  # Output: 2


# Проверочный тест:
# arr2 = [0]
# X2 = 1
# result2 = max_lower_or_equal2(arr2, X2)
# print(result2)

"""
При любой реализации бинарного поиска можно допустить ошибку. Вот как минимизировать вероятность её появления:
Используйте полуинтервалы (left = 0, right = len(arr)), а не интервалы (когда правая граница включена).
Сформулируйте для себя инвариант. Для задачи выше он будет звучать как “arr[left] не превосходит 
искомый элемент, arr[right], наоборот, превосходит”. Тогда при чтении кода вы можете проверить этот инвариант.

Именно поэтому в примере кода выше мы вынесли проверку существования искомого элемента в отдельное условие. 
Если такого элемента в массиве не существует, то инвариант при инициализации не выполнялся бы и решение было бы некорректным.
Проверяйте три простых теста:

[1, 2], ответ 1. Для задачи выше это будет arr = [1, 2], X = 1.
[1, 2], ответ 2. Для задачи выше это будет arr = [1, 2], X = 2.
Ответа нет. Для задачи выше это будет arr = [1, 2], X = 0.
"""
