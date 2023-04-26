# Сумма элементов списка
def sum(list):
  if list == []:
    return 0
  return list[0] + sum(list[1:])

lst = [5, 56, 2]
print(sum(lst))