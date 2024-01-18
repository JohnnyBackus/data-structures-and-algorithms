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
