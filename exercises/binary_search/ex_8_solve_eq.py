"""
Пусть нам нужно найти решение уравнения (x)=Y. Вычислить значение выражения x⋅log2 (x) легко, а найти решение
уравнения математически — нет. Поскольку функция (x) монотонно возрастает при x⩾ 1, можно применить бинарный поиск.
"""
from math import log2
def solve_equation(value):
    left, right = 1, value
    for _ in range(100):
        mid = (left + right) / 2
        expr_result = mid * log2(mid)
        if expr_result < value:
            left = mid
        else:
            right = mid
    return mid

result = solve_equation(10)
print(result)
