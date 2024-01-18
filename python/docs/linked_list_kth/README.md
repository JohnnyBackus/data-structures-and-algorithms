# Linked-List-Kth

Extending an implementation of a linked list to find the kth value from the end of a linked list.

## Feature Tasks

**Write the following method for the Linked List class:**

- kth from end
  - argument: a number, k, as a parameter.
  - Return the node’s value that is k places from the tail of the linked list.
  - You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process

[!Whiteboard Diagram]()

## Approach & Efficiency

**What approach did you take? Why?**

>*Answer*

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
