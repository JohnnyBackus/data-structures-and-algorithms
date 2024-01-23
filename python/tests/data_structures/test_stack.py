import pytest
from data_structures.stack import Stack
from data_structures.invalid_operation_error import InvalidOperationError



def test_exists():
    assert Stack


# @pytest.mark.skip("TODO")
# Can successfully instantiate an empty stack
def test_push_onto_empty():
    s = Stack()
    s.push("apple")
    actual = s.top.value
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully push onto a stack
def test_push_onto_full():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    actual = s.top.value
    expected = "cucumber"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully pop off the stack
def test_pop_single():
    s = Stack()
    s.push("apple")
    actual = s.pop()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully push multiple values onto a stack
def test_pop_some():
    s = Stack()

    s.push("apple")
    s.push("banana")
    s.push("cucumber")

    s.pop()

    actual = s.pop()
    expected = "banana"

    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully empty a stack after multiple pops
def test_pop_until_empty():
    s = Stack()
    s.push("apple")
    s.push("banana")
    s.push("cucumber")
    s.pop()
    s.pop()
    s.pop()
    actual = s.is_empty()
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully peek the next item on the stack
def test_peek():
    s = Stack()
    s.push("apple")
    s.push("banana")
    actual = s.peek()
    expected = "banana"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Calling peek on empty stack raises exception
def test_peek_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.peek()

    assert str(e.value) == "Method not allowed on empty collection"


# @pytest.mark.skip("TODO")
# Calling pop on an empty stack raises exception
def test_pop_empty():
    s = Stack()
    with pytest.raises(InvalidOperationError) as e:
        s.pop()

    assert str(e.value) == "Method not allowed on empty collection"
