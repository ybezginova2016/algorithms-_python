"""
D. Две фишки

Рита и Гоша играют в игру. У Риты есть n фишек, на каждой из которых написано количество очков.
Сначала Гоша называет число k, затем Рита должна выбрать две фишки, сумма очков на которых равна заданному числу.

Рите надоело искать фишки самой, и она решила применить свои навыки программирования для решения
этой задачи. Помогите ей написать программу для поиска нужных фишек.

"""
##### O(n^2) #####
from typing import List, Tuple, Optional

def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
    n = len(arr)
    for i in range(n):
        for j in range(i+1, n):
            if arr[i] + arr[j] == target_sum:
                return (arr[i], arr[j])
    return None


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    target_sum = int(input())
    return arr, target_sum

def print_result(result: Optional[Tuple[int, int]]) -> None:
    if result is None:
        print("None")
    else:
        print(result[0], result[1])

arr, target_sum = read_input()
print_result(two_sum(arr, target_sum))


lst_x = [2, 1, 5, 6, 4]
x = 6
print(two_sum(lst_x, x))

"""
In this implementation, we use two nested loops to iterate over all pairs of numbers in the list. 
We check if the sum of the current pair is equal to the target_sum. If it is, we return the pair 
as a tuple. If no pair is found, we return None.

Note that this implementation is less efficient than the one using a dictionary, 
as it has a time complexity of O(n^2), while the dictionary-based implementation 
has a time complexity of O(n).
"""

##### O(n) #####
from typing import List, Tuple, Optional

def find_sum_pair(numbers: List[int], k: int) -> Optional[Tuple[int, int]]:
    # Создаем словарь для хранения встреченных чисел и их индексов.
    nums = {}
    for i, num in enumerate(numbers):
        # Проверяем, есть ли нужное число в словаре.
        if k - num in nums:
            # Если да, то возвращаем пару чисел.
            return k - num, num
        # Если нет, то добавляем текущее число в словарь.
        nums[num] = i
    # Если не найдено пары, то возвращаем None.
    return None

n = int(input())
numbers = list(map(int, input().split()))
k = int(input())

result = find_sum_pair(numbers, k)
if result is None:
    print("None")
else:
    print(result[0], result[1])

lst_d = [2, 1, 5, 6, 4]
x = 6
print(two_sum(lst_d, x))