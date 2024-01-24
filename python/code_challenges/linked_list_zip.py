from data_structures.linked_list import LinkedList, Node


def zip_lists(list_a, list_b):
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
