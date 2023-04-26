# The bubble sort algorithm

# regular bubble sort algorithm
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

arr = [89, 75, -3, 0, 42]
print(bubble_sort(arr))

# adjusted bubble sort algorithm
def countSwaps(arr):
    n = len(arr)
    num_swaps = 0  # initialize a counter for the number of swaps
    for i in range(n):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]: # if >, then we sort in ascending order; if < - descending
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                # Увеличиваем счётчик для каждой замены
                num_swaps += 1 # increment the counter for each swap
    print("Array is sorted in", num_swaps, "swaps.")
    print('First Element: ', arr[0])
    print('Last Element: ', arr[-1])

    return arr

arr = [89, 75, -3, 0, 42]
print(countSwaps(arr))


def countSwaps(a):
    # Write your code here
    length = len(a)
    swap_count = 0
    for i in range(length - 1):
        for j in range(length - 1):
            if a[j] > a[j + 1]:
                a[j + 1], a[j] = a[j], a[j + 1]
                swap_count += 1
    print(f"Array is sorted in {swap_count} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
