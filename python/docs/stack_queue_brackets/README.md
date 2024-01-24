# Stack-Queue-Brackets

Multi-bracket Validation.

## Feature Tasks

- Write a function called validate_brackets
  - Arguments: string
  - Return: boolean
    - representing whether or not the brackets in the string are balanced
-There are 3 types of brackets:
  - Round Brackets : ()
  - Square Brackets : []
  - Curly Brackets : {}

## Whiteboard Process

[!Whiteboard Diagram](cc13_whiteboard.jpg)

## Approach & Efficiency

**What approach did you take? Why?**

- If our objective is to verify that brackets are properly paired, we can ignore all characters that are not opening or closing brackets.
- If we receive an opening bracket char, the next bracket char must be the same type of bracket's closing char OR another opening char.
- We need a data-structure to store opening chars.
  - we will need to continually reference the most recent opening bracket char
    - thus, we should store data in a structure that can use a LIFO approach to storing data
    - thus, a stack would be most appropriate.
- The function will instantiate an "opening bracket" stack.
  - it will iterate through the string.
  - it will ignore any chars that are not brackets
  - it will push all opening bracket chars to the "opening bracket" stack
  - when it comes across a closing bracket char, it will check the top of the "opening bracket" stack and verify it is an appropriate opening pair.
  - if it is not the appropriate closing bracket, it will return FALSE
  - if it the appropriate closing bracket, it will pop the opening bracket char from the "opening bracket" stack and continue to iterate through the string
  - if the function is able to iterate through the entire string, it will check the "opening bracket" stack to make sure it is empty
    - if not empty, it will return FALSE because it means there is at least one missing closing bracket.
    - if the stack is empty, the function will return TRUE

**What is the Big O space/time for this approach?**

>*These method has a space time complexity of O(n). The function will perform the operation above once per char in the string until it returns False or runs through the entire string and returns True.*

## Resources

- [CodeFellows Technical Whiteboarding Guidelines](https://codefellows.github.io/common_curriculum/challenges/code/whiteboarding)

- used ChatGPT to figure out how to reference a dict value by key.
  - [ChatGPT chat](https://chat.openai.com/share/2f6ea5ef-78aa-481d-95bd-2b09697b9b94)
- GitHub copilot helps with syntax errors.

## Solution

'''
def multi_bracket_validation(string):
    open_brackets_stack = Stack()
    open_brackets = ['[', '{', '(']
    close_brackets = [']', '}', ')']
    pairs = {']':'[', '}':'{', ')':'('}
    for char in string:
        if char in open_brackets:
            open_brackets_stack.push(char)
        elif char in close_brackets:
            if open_brackets_stack.is_empty(): # checks if closing bracket comes before opening bracket
                return False
            elif pairs[char] == open_brackets_stack.top.value:
                open_brackets_stack.pop()
            else:
                return False
    if open_brackets_stack.is_empty():
        return True
    else:
        return False
'''
