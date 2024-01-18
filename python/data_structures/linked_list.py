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

    def append(self, value):
        node = Node(value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = node

    def insert_before(self, value, new_value):
        node = Node(new_value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.next.value != value:
            current = current.next
        node.next = current.next
        current.next = node

    def insert_after(self, value, new_value):
        node = Node(new_value)
        if not self.head:
            self.head = node
            return
        current = self.head
        while current.value != value:
            current = current.next
        node.next = current.next
        current.next = node

    def kth_from_end(self, k):
        if k < 0:
            raise TargetError("Target must be a positive integer")
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        if k > count:
            raise TargetError("Target is out of range")
        current = self.head
        for i in range(count - k -1):
            current = current.next
        return current.value

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


class TargetError:
    pass
