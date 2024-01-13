# Linked-List

- Create a Node class that has properties for the value stored in the Node, and a pointer to the next Node.
- Create a Linked List class
- Within your Linked List class, include a head property.
  - Upon instantiation, an empty Linked List should be created.
- The class should contain the following methods
  - insert
    - Arguments: value
    - Returns: nothing
    - Adds a new node with that value to the head of the list with an O(1) Time performance.
  - includes
    - Arguments: value
    - Returns: Boolean
      - Indicates whether that value exists as a Node’s value somewhere within the list.
  - to string
    - Arguments: none
    - Returns: a string representing all the values in the Linked List, formatted as:
    - `{ a } -> { b } -> { c } -> NULL`

## Whiteboard Process

- not applicable for this code challenge

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
