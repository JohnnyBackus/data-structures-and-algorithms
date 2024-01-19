# Linked-List-Zip

Extending an implementation of a linked list to zip two linked-lists together

## Feature Tasks

**Write the following method for the Linked List class:**

- zip lists
  - Arguments: 2 linked lists
  - Return: New Linked List, zipped as noted below
  - Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the the zipped list.
  - Try and keep additional space down to O(1)
  - You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.

## Whiteboard Process

[!Whiteboard Diagram](List_zip.png)

## Approach & Efficiency

**What approach did you take? Why?**

>*The examples provided take two linked-lists as arguments. The output is a new linked-list where the head is the head of list1 followed by the head of list 2 with nodes alternating until one of the linked lists is complete. The remainder of the longer list is appended to the end of the combined list.*
>*We can use similar methodology as the append method.
>*Update: this was a lot harder than I anticipated.*

**What is the Big O space/time for this approach?**

>*This method has a space time complexity of Big O(a + b). Complexity grows linearly based on the length of the linked lists.*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

- [ChatGPT](https://chat.openai.com/share/f400a014-4a22-401a-a79f-30d7cfb37a1b)

## Solution

```def zip_lists(self, list_a, list_b):
        new_list = LinkedList()
        current_a = list_a.head
        current_b = list_b.head
        current_new = new_list.head

        while current_a and current_b:
            if not current_new:
                new_node = Node(current_a.value)
                new_list.head = new_node
                current_new = new_list.head
                current_a = current_a.next
            else:
                current_new.next = Node(current_b.value)
                current_b = current_b.next
                current_new = current_new.next
                current_new.next = Node(current_a.value)
                current_a = current_a.next
                current_new = current_new.next

        while current_a:
            if not current_new:
                new_node = Node(current_a.value)
                new_list.head = new_node
                current_new = new_list.head
                current_a = current_a.next
            else:
                current_new.next = Node(current_a.value)
                current_a = current_a.next
                current_new = current_new.next

        while current_b:
            if not current_new:
                new_node = Node(current_b.value)
                new_list.head = new_node
                current_new = new_list.head
                current_b = current_b.next
            else:
                current_new.next = Node(current_b.value)
                current_b = current_b.next
                current_new = current_new.next
        return new_list
  ```
