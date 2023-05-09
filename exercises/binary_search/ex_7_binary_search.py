#  Есть упорядоченный массив целых чисел arr, нужно определить, есть ли в нём число X.
def binary_search(arr, target):
    left_idx, right_idx = 0, len(arr)
    while left_idx < right_idx:
        mid_idx = (left_idx + right_idx) // 2
        if arr[mid_idx] == target:
            return True
        elif arr[mid_idx] < target:
            left_idx = mid_idx + 1
        else:
            right_idx = mid_idx
    return False

arr = [1, 3, 5, 7, 9]
target = 5
result = binary_search(arr, target)
print(result)
