# Stack-Queue-Pseudo

Implement a Queue using two Stacks.

## Feature Tasks

- Create a new class called pseudo queue.
  - Do not use an existing Queue.
  - Instead, this PseudoQueue class will implement our standard queue interface (the two methods listed below),
  - Internally, utilize 2 Stack instances to create and manage the queue

- Methods:
  - enqueue
    - Arguments: value
    - Inserts a value into the PseudoQueue, using a first-in, first-out approach.
  - dequeue
    - Arguments: none
    - Extracts a value from the PseudoQueue, using a first-in, first-out approach

## Whiteboard Process

[!Whiteboard Diagram](cc11_whiteboard.jpg)

## Approach & Efficiency

**What approach did you take? Why?**

- Since a Queue has a front and a back, I imagine we will need to use the top of one stack to represent the front while the top of the other would represent the back.
  - The .enqueue() method will need to initiate the PQ using the Stack class and then building with the .push() method
  - The .dequeue() method will need to create a new "dequeue stack" by using the .pop() method on the "enqueue stack" and pushing to the "dequeue stack" until the "enqueue stack" is empty and then pop from the "dequeue stack".
  - If we want to enqueue after that, we need to reverse the process so that we always push to the top of the "enqueue stack"
  - The bottom of the "enqueue stack" (if it is populated) is always the front of the PQ

**What is the Big O space/time for this approach?**

>*These methods have a space time complexity of O(n). The longer the stack, the longer it will take to "re-stack". Each dequeque will require going through the entire stack.*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

- used GitHub copilot for prompting on syntax for methods.

## Solution

'''
class PseudoQueue:
  def __init__(self):
      self.enqueue_stack = Stack()
      self.dequeue_stack = Stack()

  def enqueue(self, value):
      enqueue_stack = self.enqueue_stack
      dequeue_stack = self.dequeue_stack
      while dequeue_stack.top is not None:
          enqueue_stack.push(dequeue_stack.pop())
      enqueue_stack.push(value)

  def dequeue(self):
      enqueue_stack = self.enqueue_stack
      dequeue_stack = self.dequeue_stack
      while enqueue_stack.top is not None:
          dequeue_stack.push(enqueue_stack.pop())
      return dequeue_stack.pop()
'''
