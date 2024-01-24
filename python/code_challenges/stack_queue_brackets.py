from data_structures.stack import Stack


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

