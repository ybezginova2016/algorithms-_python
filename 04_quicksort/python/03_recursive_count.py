# Функция для подсчета элементов в списке

def count(list):
  if list == []:
    return 0
  return 1 + count(list[1:])

lst = [5, 56, 2]
print(count(lst))