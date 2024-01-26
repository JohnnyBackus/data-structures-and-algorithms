# Trees

Implementing a new Tree and Binary Search Tree

## Features

- Node
  - Create a Node class that has properties for the value stored in the node, the left child node, and the right child node.

- Binary Tree
  - Create a Binary Tree class
    - Define a method for each of the depth first traversals:
      - pre order
      - in order
      - post order
  - Each depth first traversal method should return an array of values, ordered appropriately.

- Binary Search Tree
  - Create a Binary Search Tree class
    - This class should be a sub-class (or your languages equivalent) of the Binary Tree Class, with the following additional methods:
    - Add
      - Arguments: value
      - Return: nothing
      - Adds a new node with that value in the correct location in the binary search tree.
    - Contains
      - Argument: value
      - Returns: boolean indicating whether or not the value is in the tree at least once.

## Whiteboard Process

- not applicable for this code challenge

## Approach & Efficiency

**What approach did you take? Why?**

>*not applicable*

**What is the Big O space/time for this approach?**

>*The "contains" method in the BinarySearchTree class will be Big O(n)*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

## Solution

```
class BinaryTree:

    def __init__(self, root=None):
        self.root = root

    def pre_order(self):

        def traverse(node):
            own_value = [node.value] if node else []
            left_value = traverse(node.left) if node.left else []
            right_value = traverse(node.right) if node.right else []
            return own_value + left_value + right_value

        return traverse(self.root)

    def in_order(self):

        def traverse(node):
            own_value = [node.value] if node else []
            left_value = traverse(node.left) if node.left else []
            right_value = traverse(node.right) if node.right else []
            return left_value + own_value + right_value

        return traverse(self.root)

    def post_order(self):

        def traverse(node):
            own_value = [node.value] if node else []
            left_value = traverse(node.left) if node.left else []
            right_value = traverse(node.right) if node.right else []
            return left_value + right_value + own_value

        return traverse(self.root)


class BinarySearchTree(BinaryTree):
  # don't need __init__ if not changing anything from super class

    def add(self, value):
        node = Node(value)
        if self.root is None:
            self.root = node
            return

        def traverse(node, new_node):
            if new_node.value < node.value:
                if node.left is None:
                    node.left = new_node
                    return
                else:
                    traverse(node.left, new_node)
            elif new_node.value > node.value:
                if node.right is None:
                    node.right = new_node
                else:
                    traverse(node.right, new_node)

        return traverse(self.root, node)


    def contains(self, value):
        if self.root is None:
            raise TargetError(Exception("Tree is empty"))

        def traverse(node, value):
            if value == node.value:
                return True
            if value < node.value:
                if node.left is None:
                    return False
                else:
                    return traverse(node.left, value)  # Add return statement
            elif value > node.value:
                if node.right is None:
                    return False
                else:
                    return traverse(node.right, value)  # Add return statement

        return traverse(self.root, value)


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TargetError(BaseException):
    pass
```
