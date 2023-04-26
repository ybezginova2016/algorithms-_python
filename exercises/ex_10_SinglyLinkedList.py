##### Односвязный список #####
##### Singly Linked List ######

"""
Односвязный список (Singly Linked List) - это структура данных, которая состоит из
узлов (Node), каждый из которых содержит значение (data) и ссылку (pointer) на
следующий узел списка. Последний узел списка ссылается на специальное значение
None, обозначающее конец списка.

Преимущество односвязного списка заключается в том, что добавление и удаление
элементов в начале списка происходит очень быстро (O(1)), поскольку не требуется
копирование значений и сдвиг всех элементов. Однако, доступ к произвольному
элементу списка происходит медленнее, поскольку для этого нужно
последовательно перебрать все элементы от начала списка.
Для определения, есть ли цикл в связном списке, можно
использовать алгоритм "быстрый и медленный указатели"
(Floyd's cycle-finding algorithm). Алгоритм заключается
в том, что имеется два указателя - "быстрый" и "медленный",
которые двигаются по списку с разными скоростями.
Если в списке есть цикл, то эти два указателя рано
или поздно встретятся.

"""
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, data):
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == data:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next

    def print_list(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

def hasCycle(head):
    if head is None:
        return False

    slow = head
    fast = head.next

    while slow != fast:
        if fast is None or fast.next is None:
            return False
        slow = slow.next
        fast = fast.next.next

    return True

"""
В этой реализации передается указатель на начало списка head. 
Создаются два указателя slow и fast, которые изначально 
указывают на начало списка. Пока slow и fast не встретятся, 
slow перемещается на одну позицию за каждую итерацию цикла, 
а fast перемещается на две позиции за каждую итерацию цикла. 

Если список содержит цикл, то рано или поздно slow и fast 
встретятся, и функция вернет значение True. Если цикла в 
списке нет, то функция вернет значение False.
"""

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

# Создаем связный список с циклом
head = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)
node5 = Node(5)
head.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node2

# Вызываем функцию для проверки наличия цикла
print(hasCycle(head)) # True
