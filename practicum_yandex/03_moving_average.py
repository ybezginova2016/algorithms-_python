"""
C. Скользящее среднее

Вам дана статистика по числу запросов в секунду к вашему любимому рекомендательному сервису.
Измерения велись n секунд.
В секунду i поступает qi запросов.

Примените метод скользящего среднего с длиной окна k к этим данным и выведите результат.

### optimized 1 ###

функция скользящее_среднее(timeseries, K):
    result = []  # Пустой массив.
    для begin_index из [0 .. len(timeseries) - K]:
        end_index = begin_index + K
        # Просматриваем окно шириной K.
        current_sum = 0
        для каждого v из timeseries[begin_index .. end_index):
            current_sum += v
        current_avg = current_sum / K
        result.добавить(current_avg)
    вернуть result

### optimized 2 ###

функция скользящее_среднее(timeseries, K):
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = сумма элементов timeseries[0..K)
    result.добавить(current_sum / K)
    для i из [0 .. len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i+K]
        current_avg = current_sum / K
        result.добавить(current_avg)
    вернуть result

"""
from typing import List, Tuple

def moving_average(timeseries: List[int], K: int) -> List[float]:
    result = []  # Пустой массив.
    # Первый раз вычисляем значение честно и сохраняем результат.
    current_sum = sum(timeseries[:K])
    result.append(current_sum / K)
    for i in range(len(timeseries) - K):
        current_sum -= timeseries[i]
        current_sum += timeseries[i + K]
        current_avg = current_sum / K
        result.append(current_avg)
    return result

def read_input() -> Tuple[List[int], int]:
    n = int(input())
    arr = list(map(int, input().strip().split()))
    window_size = int(input())
    return arr, window_size

arr, window_size = read_input()
print(" ".join(map(str, moving_average(arr, window_size))))
