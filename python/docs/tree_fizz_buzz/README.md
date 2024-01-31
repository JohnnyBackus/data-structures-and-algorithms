# Tree-Breadth-First

Conduct “FizzBuzz” on a k-ary tree while traversing through it to create a new tree.

## Features

- Write a function called fizz buzz tree
  - Arguments: k-ary tree
  - Return: new k-ary tree
- Determine whether or not the value of each node is divisible by 3, 5 or both. Create a new tree with the same structure as the original, but the values modified as follows:
  - If the value is divisible by 3, replace the value with “Fizz”
  - If the value is divisible by 5, replace the value with “Buzz”
  - If the value is divisible by 3 and 5, replace the value with “FizzBuzz”
  - If the value is not divisible by 3 or 5, simply turn the number into a String.

## Whiteboard Process

- [Whiteboard](cc18whiteboard.png)

## Approach & Efficiency

**What approach did you take? Why?**

*We must return a new k-ary tree, so we will create one using the KaryTree's clone method and then modify the clone:*

- Will assume original k-ary tree values are integers
- Clone will have string values
- Will need a "traverse-style" method
  - will start at the clone's root
  - will assess each node value to be a multiple of 3, 5, or both
  - will replace node value as appropriate
    - "Fizz" if val%3 == 0
    - "Buzz" if val%5 ==0
    - "FizzBuzz"if val%15 ==0
    - else: str(val)
  - KaryTree node uses self.children[i] as pointers
  - can use a for loop of the children and call this method again on each of them
  - will return the clone tree when complete

**What is the Big O space/time for this approach?**

>*This function has a space and time complexity of O(n). It will iterate twice through every node (once when cloning and again when traversing), so technically O(2n), but we drop constants. It will use O(n) memory for the clone.*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

## Solution

```
def fizz_buzz_tree(tree):
  new_tree = tree.clone()

  def traverse(node):
    if node.value%15 == 0:
      node.value = "FizzBuzz"
    elif node.value%5 == 0:
      node.value = "Buzz"
    elif node.value%3 == 0:
      node.value = "Fizz"
    else:
      node.value = str(node.value)
    if node.children:
      for child in node.children:
        traverse(child)

  traverse(new_tree.root)

  return new_tree
```
