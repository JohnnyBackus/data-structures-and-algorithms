from data_structures.invalid_operation_error import InvalidOperationError

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None # the pointer initially points to Null, and will be assigned in the queue

class Queue:
    def __init__(self):
        self.front = None # default value for front and back is None so that an empty queue can exist
        self.back = None

    def enqueue(self, value):
        '''Adds a new node to the back of the queue; does not return anything'''
        node = Node(value) # create a new node
        if self.back is None: # if queue is empty, assign front and back to the new node
            self.front = node
            self.back = node
        else: # if queue is not empty, give the current back a .next value and add assign the new node to the back
            self.back.next = node
            self.back = node

    def dequeue(self):
        '''Removes the node from the front of the queue and returns the node's value'''
        if self.front:
            value = self.front.value
            self.front = self.front.next # reassign front to the next node so front will no longer be referencing anything in the queue
            return value
        else:
            raise InvalidOperationError() # if queue is empty, raise error

    def peek(self): # does not alter the queue, just reveals value of the front
        if self.front:
            return self.front.value
        else:
            raise InvalidOperationError() # if queue is empty, raise error

    def is_empty(self):
        if self.front: #if stack has a value, return False
            return False
        return True
