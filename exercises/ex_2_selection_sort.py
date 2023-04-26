# Код сортировки музыкального списка, но написанный ниже код делает нечто очень похожее: он выполняет сортировку массива по возрастанию.

arr = [4, 56, -3, 676, 0, 23]

# ищем наименьший элемент в массиве или его индекс
def findSmallest(arr):
    # считаем первый элемент массивы наименьшим
    smallest = arr[0]
    # smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest
    # return smallest_index

print(findSmallest(arr))

# пишем алгоритм сортировки
def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]
    return nums

print(selection_sort(arr))
