import numpy as np

spots = np.array([[2,3,4,5,6,7], # имя переменной spots по-английски значит «пятна»
    [3,4,5,6,7,8],
    [4,5,6,7,8,9],
    [5,6,7,8,9,10],
    [6,7,8,9,10,11],
    [7,8,9,10,11,12]])

print(spots)

# Подсчитаем, сколько раз встречается каждая сумма пятен.
# Создадим словарь spot_counts (от англ. the counting of spots,
# «подсчёт пятен»). Ключи — суммы пятен, а значения —
# количество комбинаций, приводящих к этой сумме.

spots_count = {}

for i in range(0, 6):
    for j in range(0, 6):
        if spots[i][j] not in spots_count.keys():
            spots_count[spots[i][j]] = 1 # обращение по ключу
        else:
            spots_count[spots[i][j]] += 1

print(spots_count)

# spots[i][j] - это элемент матрицы, находящийся на i-й
# строке и j-м столбце. Код проверяет, сколько раз каждый
# элемент матрицы встречается в ней.
print()
# dictionary comprehension (англ. «описание словаря»).
spot_probs={k:spots_count[k]/36 for k in spots_count}
print(spot_probs)

# using for loop

spot_probs = {}

for k in spots_count:
    spot_probs[k] = spots_count[k] / 36

print(spot_probs)