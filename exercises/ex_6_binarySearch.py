"""
Имеется отсортированный список из 128 имен, и вы ищете в нем значение методом бинарного поиска.
Какое максимальное количество проверок для этого может потребоваться?
"""
def binary_search_name(list, item):
    low = 0
    high = len(list) - 1
    count = 0
    while low <= high:
        count += 1
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1

        else:
            low = mid + 1

    return None, count


name_list = ['Yulia', 'Maria', 'Vanja', 'Vlada'] * 32
name_sorted = sorted(name_list)
print(name_sorted)

result, count = binary_search_name(name_sorted, 'Yulia')
print(f"The index of the item is {result} and the number of checks is {count}")
