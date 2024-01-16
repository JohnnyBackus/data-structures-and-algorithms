# Linked-List-Insertion

Extending an implementation

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

[!Whiteboard Diagram]()

## Approach & Efficiency

**What approach did you take? Why?**

>*not applicable; follow python rules for creating Node and LinkedList objects.*

**What is the Big O space/time for this approach?**

>*not applicable*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

- Received help from TAs Kjell and Tammy regarding understanding of terminology and verifying sample tests met requirements of code challenge (vs needing to write some of our own tests)

## Solution

```class Node:
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

    return pass```
