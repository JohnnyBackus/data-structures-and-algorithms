# Stack and Queue

Using a Linked List as the underlying data storage mechanism, implement both a Stack and a Queue

## Node

- Create a Node class that has properties for the value stored in the Node, and a pointer to the next node.

## Stack

- Create a Stack class that has a top property. It creates an empty Stack when instantiated.
  - This object should be aware of a default empty value assigned to top when the stack is created.
  - The class should contain the following methods:
  - push
    - Arguments: value
    - adds a new node with that value to the top of the stack with an O(1) Time performance.
  - pop
    - Arguments: none
    - Returns: the value from node from the top of the stack
    - Removes the node from the top of the stack
    - Should raise exception when called on empty stack
  - peek
    - Arguments: none
    - Returns: Value of the node located at the top of the stack
    - Should raise exception when called on empty stack
  - is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the stack is empty.

## Queue

- Create a Queue class that has a front property. It creates an empty Queue when instantiated.
  - This object should be aware of a default empty value assigned to front when the queue is created.
  - The class should contain the following methods:
  - enqueue
    - Arguments: value
    - adds az new node with that value to the back of the queue with an O(1) Time performance.
  - dequeue
    - Arguments: none
    - Returns: the value from node from the front of the queue
    - Removes the node from the front of the queue
    - Should raise exception when called on empty queue
  - peek
    - Arguments: none
    - Returns: Value of the node located at the front of the queue
    - Should raise exception when called on empty stack
  - is empty
    - Arguments: none
    - Returns: Boolean indicating whether or not the queue is empty

## Whiteboard Process

- not applicable for this code challenge

## Approach & Efficiency

**What approach did you take? Why?**

>*not applicable; follow python rules for creating Node and Stack and Queue Classes.*

**What is the Big O space/time for this approach?**

>*not applicable*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

## Solution

``` *class Stack followed by class Queue*

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

```
