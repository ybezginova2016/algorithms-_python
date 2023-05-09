# ПЛОХО!!!
# Find a certain element in the list
def binary_search(list, item):
    low = 0
    high = len(list) - 1
    while low <= high:
        mid = (low+high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return item

lst = [167, 5, 64, 19]
print(binary_search(lst, 19))
