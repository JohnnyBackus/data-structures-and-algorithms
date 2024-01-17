# Linked-List-Insertion

Extending an implementation of a linked list to allow various insertion methods.

## Feature Tasks

**Write the following methods for the Linked List class:**

- append
  - arguments: new value
  - adds a new node with the given value to the end of the list
- insert before
  - arguments: value, new value
  - adds a new node with the given new value immediately before the first node that has the value specified
- insert after
  - arguments: value, new value
  - adds a new node with the given new value immediately after the first node that has the value specified

## Whiteboard Process

[!Whiteboard Diagram](python/code_challenges/linked_list_insertions/cc06_whiteboard.jpg)

## Approach & Efficiency

**What approach did you take? Why?**

>* Each method is very similar:
 - We will use the Node class attributes of .next and .value to find the target value in the linked list.
 - The .append method is simpler because the    .value attribute is not needed.
- First, a new node is created with the args
- With all three methods, the new node verifies a head exists. If not, it will assign itself to the head.
 self.head = node and then exit the code.
- if self.head has a value, the code will assign the variable "current" to self.head so that node attributes are now accessible.
- while current.next exists, we can continue to reassign current to current.next to move along the list.
 - We will be at our target when current.next is Null for the append method or when current.next.value = target value for the others.*

**What is the Big O space/time for this approach?**

>*These methods have a space time complexity of O(n). The longer the linked list, the longer it will potentially take to reach the target insert or append location.  The insert methods have potential to be fast depending on where in the list the new value is to be inserted. The append method will always run through all values in the linked list to reach the end.*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

- used GitHub copilot for prompting on syntax for methods.

## Solution

```def append(self, value):
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
        ```
