from data_structures.invalid_operation_error import InvalidOperationError


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # the pointer initially points to Null, and will be assigned in the stack


class Stack:
    def __init__(self):
        self.top = None # default value is None so that an empty stack can exist

    def push(self, value): # same approach as the linked list push method
        node = Node(value)
        node.next = self.top
        self.top = node

    def pop(self): # reassign top to the next node so top will no longer be referencing anythig in the stack
        if self.top:
            value = self.top.value
            self.top = self.top.next
            return value
        else:
            raise InvalidOperationError("Method not allowed on empty collection") # if stack is empty, return None

    def peek(self): # does not alter the stack, just reveals value of the top
        if self.top:
            return self.top.value
        else:
            raise InvalidOperationError("Method not allowed on empty collection")


    def is_empty(self):
        if self.top: #if stack has a value, return False
            return False
        return True


# class TargetError(Exception):
#     pass


# print(InvalidOperationError(e_message))
