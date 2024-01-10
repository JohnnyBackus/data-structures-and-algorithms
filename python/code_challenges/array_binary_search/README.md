# Array-Binary-Search

Write a function called BinarySearch which takes in 2 parameters: a sorted list and the search key. Without utilizing any of the built-in methods available to Python, return the index of the list’s element that is equal to the value of the search key, or -1 if the element is not in the list.

## Whiteboard Process

<![Whiteboard Solution]()

## Approach & Efficiency

**What approach did you take? Why?**

>*I wanted to use a binary search method by finding the middle of the list (using len//2) and see if the value at this index position matched the search key's value. If yes, I would return the index. If not, I would see if the search key value is higher or lower and then repeat the process on the half of the list where the search key's value lies. This process should work because the list is ordered.*

**What is the Big O space/time for this approach?**

>*The max number of searches should be log base(2) of n this I think this is still considered a Big O(n) since the runtime will still increase linearly (just more slowly than if the max number of searches was simply n). I still don't know if I am answering this question correctly, but I think space requirements would be negligible since we aren't adding any input?*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

## Solution

```def binary_search(list, search_key):

    return search_key_index```
