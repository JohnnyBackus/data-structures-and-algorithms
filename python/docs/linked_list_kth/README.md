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

>*TDD. I figured I would need to keep a count of the nodes in the linked-list and iterate to find the end. So I started there and then just started trying to make tests pass. It wasn't until I solved one of the last tests I attempted where I needed to store the value of the last node that I realized I probably could have stored all of the values as I iterated through the linked-list in a regular list or dictionary, but maybe that defeats the purpose of using a linked list and would have been inefficient use of memory.*

**What is the Big O space/time for this approach?**

>*This method has a space time complexity of O(n + k). It will have to run through the entire linked list to find the end. Most of the time, it will have to partially run through it again up to the node at position (n - k).*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

- used GitHub copilot for prompting on syntax and how to use TargetError. Also prompted use of for i in range loop.

## Solution

```def kth_from_end(self, k):
  if k < 0:
      raise TargetError(Exception("k cannot be a negative integer"))
  current = self.head
  count = 0
  last_value = 0
  while current:
      count += 1
      last_value = current.value
      current = current.next
  if k == 0:
      return last_value
  if k == (count - 1): # Where k is one less than the length of the list
      return self.head.value
  if k > (count - 1):
      raise TargetError(Exception("k is equal to or greater than the length of the linked list"))
  current = self.head
  for i in range(count - (k + 1)): # +1 needed to account for range starting at 0
      current = current.next
  return current.value
  ```
