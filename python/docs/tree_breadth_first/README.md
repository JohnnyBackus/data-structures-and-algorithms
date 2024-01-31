# Tree-Breadth-First

Breadth-first Traversal

## Features

- Write a function called breadth first
  - Arguments: tree
  - Return: list of all values in the tree, in the order they were encountered
  Traverse the input tree using a Breadth-first approach

## Whiteboard Process

- [Whiteboard](cc17whiteboard.png)

## Approach & Efficiency

**What approach did you take? Why?**

>*As visualized during lecture, I wanted to use a queue to store copies of nodes as the tree is traversed.*

- I need to store the value of the node at the front of the queue before dequeing
  - this could be stored in a list that will be returned when the function is done running
- Also need to check the left and right pointers and enqueue those nodes in order if present
- Repeat

**What is the Big O space/time for this approach?**

>*This method will have both a space and time complexity Big O(n). The method will iterate through every node in the tree once and store a value for each node.*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

## Solution

```
def find_maximum_value(self):

  def traverse(node, val):
    max_val = val
    if node.value > max_val:
        max_val = node.value
    if node.left:
        return traverse(node.left, max_val)
    elif node.right:
        return traverse(node.right, max_val)
    return max_val

  return traverse(self.root, self.root.value)
```
