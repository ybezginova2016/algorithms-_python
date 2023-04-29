lst_x = [2, 1, 5, 6, 4]

x = 6
def twosum(numbers, X):
    for i in range(len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == X:
                return numbers[i], numbers[j]
    # return None, None
    raise ValueError("Пара не найдена")

print(twosum(lst_x, x))