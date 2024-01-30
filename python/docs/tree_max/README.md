# Tree-Max

Find the Maximum Value in a Binary Tree

## Features

Write the following method for the Binary Tree class

- find maximum value
  - Arguments: none
  - Returns: number
  - Finds the maximum value stored in the tree. You can assume that the values stored in the Binary Tree will be numeric.

## Whiteboard Process

- not completed

## Approach & Efficiency

**What approach did you take? Why?**

>*Use recursion of a traverse method in a way similar to how it was used for the pre-order, post-order, and in-order methods*

- I need to store max value
  - this could be stored as a global variable, but then would be out of scope if used in the traverse method
  - better to store inside traverse method
  - can pass max_value as parameter of traverse method

**What is the Big O space/time for this approach?**

>*This method will be Big O(n)*

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
