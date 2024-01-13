class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def insert(self, value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def includes(self, value):
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def __str__(self):
        output = ''
        current = self.head
        while current:
            output += f'{{ {current.value} }} -> '
            current = current.next
        output += 'NULL'
        return output

# ------------ Code below was used to help me visualize node and linked list ------------

# Node("apple")
# Node("banana")
# print(Node("apple"))
# print(Node("banana"))

# def string_double():
#     linked_list = LinkedList()
#     linked_list.insert("apple")
#     print(str(linked_list))
#     linked_list.insert("banana")
#     print(str(linked_list))

# string_double()
