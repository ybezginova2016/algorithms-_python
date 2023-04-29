x = 10
# При попытке изменить переменную x в sum_func() будет создана новая локальная переменная
def sum_func(x):
    x += 5
    return x

def first_func():
    global x
    sum_func(x)

first_func()
print(x)