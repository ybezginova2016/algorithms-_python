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

arr = [1, 2, 4, 7, 9]
value = 6
result = max_lower_or_equal(arr, value)
print(result)  # Output: 2
