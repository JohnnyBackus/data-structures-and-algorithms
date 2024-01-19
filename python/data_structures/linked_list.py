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
            raise TargetError(Exception("k cannot be a negative integer"))
        current = self.head
        node_count = 0
        last_value = 0
        while current:
            node_count += 1
            last_value = current.value
            current = current.next
        if k == 0:
            return last_value
        if k == (node_count - 1): # Where k is one less than the length of the list
            return self.head.value
        if k > (node_count - 1):
            raise TargetError(Exception("k is equal to or greater than the length of the linked list"))
        current = self.head
        for i in range(node_count - (k + 1)): # +1 needed to account for range starting at 0
            current = current.next
        return current.value

    def zip_lists(self, list_a, list_b):
        new_list = LinkedList()
        current_a = list_a.head
        current_b = list_b.head
        current_new = new_list.head

        while current_a and current_b:
            if not current_new:
                new_node = Node(current_a.value)
                new_list.head = new_node
                current_new = new_list.head
                current_a = current_a.next
            else:
                current_new.next = Node(current_b.value)
                current_b = current_b.next
                current_new = current_new.next
                current_new.next = Node(current_a.value)
                current_a = current_a.next
                current_new = current_new.next

        while current_a:
            if not current_new:
                new_node = Node(current_a.value)
                new_list.head = new_node
                current_new = new_list.head
                current_a = current_a.next
            else:
                current_new.next = Node(current_a.value)
                current_a = current_a.next
                current_new = current_new.next

        while current_b:
            if not current_new:
                new_node = Node(current_b.value)
                new_list.head = new_node
                current_new = new_list.head
                current_b = current_b.next
            else:
                current_new.next = Node(current_b.value)
                current_b = current_b.next
                current_new = current_new.next
        return new_list

    def __str__(self):
        output = ''
        current = self.head
        while current:
            output += f'{{ {current.value} }} -> '
            current = current.next
        output += 'NULL'
        return output


class TargetError(BaseException):
    pass

# ------------ Code below was used to help me visualize node and linked list ------------

if __name__ == "__main__":


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

# equal length linked lists
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    print("list_a:", list_a)
    print("list_b:", list_b)

    list_c = LinkedList()
    print("list_c:", list_c.zip_lists(list_a, list_b))

# list_a shorter
    list_a = LinkedList()
    for value in reversed([1, 2]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    list_c = LinkedList()
    print("list_a:", list_a)
    print("list_b:", list_b)
    print("list_c:", list_c.zip_lists(list_a, list_b))

# list_b shorter
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)

    list_b = LinkedList()
    for value in reversed(["a", "b"]):
        list_b.insert(value)

    list_c = LinkedList()
    print("list_a:", list_a)
    print("list_b:", list_b)
    print("list_c:", list_c.zip_lists(list_a, list_b))

# list_a empty
    list_a = LinkedList()

    list_b = LinkedList()
    for value in reversed(["a", "b", "c"]):
        list_b.insert(value)

    list_c = LinkedList()
    print("list_a:", list_a)
    print("list_b:", list_b)
    print("list_c:", list_c.zip_lists(list_a, list_b))

# list_b empty
    list_a = LinkedList()
    for value in reversed([1, 2, 3]):
        list_a.insert(value)
    list_b = LinkedList()

    list_c = LinkedList()
    print("list_a:", list_a)
    print("list_b:", list_b)
    print("list_c:", list_c.zip_lists(list_a, list_b))
