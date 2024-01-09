# Array-Insert-Shift

Creating a function that given a list and value inserts the value into the middle of the list (or to the right of the middle point for lists with an odd number of elements)

## Whiteboard Process

<![Whiteboard Solution]((solution.png))

## Approach & Efficiency

**What approach did you take? Why?**

>*I wanted to find the middle using len/2 and simply append the new value to the right of this index. Since the .insert method was off limits, I thought that creating two lists and rejoining them would be a straightforward solution.*

**What is the Big O space/time for this approach?**

>*We will need to run through entire list during for loop thus giving us a Big O(n): the run time will increase linearly with the length of the list. Runtimes for other lines of code such as the list contantentation are not affected by n and thus are negligible. Space is also negligible as we are only adding one value to the existing list.*

## Resources

- Used ChatGPT to recall how to join lists - they can be cancantanated in Python in lieu of a .join method

## Solution

```def insert_shift_array(list, val):
    first_half = []
    second_half = []
    for i in range(len(list)):
        if i <= len(list)//2:
            first_half.append(list[i])
        else:
            second_half.append(list[i])
    first_half.append(val)
    new_list = first_half + second_half
    return new_list```
