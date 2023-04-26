##### .sort() #####
# .sort() есть только у списков!
# У списков имеется встроенный метод для сортировки, но у других
# итерируемых типов Python (например, у ключей словаря) метода sort нет.

# len(string) возвращает количество символов в строке
def compare_num_of_chars(string1):
    """передает методу сортировки длину строк (вместо самих строк)"""
    return len(string1)

str_ex = 'Yulia'

print(compare_num_of_chars(str_ex))

"""
После того как вы определите ключевую функцию, остается передать ее методу 
sort с именем key. Так как функции являются объектами Python, они могут 
передаваться функциям как любые другие объекты Python.
"""

def compare_num_chars(string1):
    return len(string1)

word_list = ['Python', 'is', 'better', 'than', 'C++']
word_list.sort()
print(word_list)

# Output: ['C++', 'Python', 'better', 'is', 'than'] ==>
# ==> список упорядочен в лексикографическом порядке (верхний регистр предшествует нижнему),

word_list = ['Python', 'is', 'better', 'than', 'C++']
word_list.sort(key=compare_num_chars)
print(word_list)

# Output: ['is', 'C++', 'than', 'Python', 'better'] ==>
# ==> список упорядочен по возрастанию количества символов.

##### Функция sorted() #####
x = (4, 3, 1, 2)
y = sorted(x)
print(y)

z = sorted(x, reverse=True)
print(z)

##### EXAMPLE 1 #####

"""
Имеется список, каждый элемент которого также является списком: 
[[1, 2, 3], [2, 1, 3], [4, 0, 1]]. Допустим, вы хотите отсортировать 
этот список по второму элементу каждого списка, чтобы получить результат 
[[4, 0, 1], [2, 1, 3], [1, 2, 3]].
"""

lst = [[1, 2, 3], [2, 1, 3], [4, 0, 1]]
"""
To sort the list based on the second element of each sublist, you can 
use the sorted() function and specify a sorting key function that 
returns the second element of each sublist.
"""
a_sort = sorted(lst, key=lambda x: x[1]) # сортировка по второму элементу
b_sort = sorted(lst)
print(a_sort) # output: [[4, 0, 1], [2, 1, 3], [1, 2, 3]]
print(b_sort) # output: [[1, 2, 3], [2, 1, 3], [4, 0, 1]]

# Если вы хотите отсортировать каждый внутренний список по возрастанию,
# то вам нужно применить сортировку к каждому внутреннему списку
# в отдельности.

for sublist in lst:
    sublist.sort()

print(lst)
# Output: [[1, 2, 3], [1, 2, 3], [0, 1, 4]]