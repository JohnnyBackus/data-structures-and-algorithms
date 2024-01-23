import pytest
from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError



def test_exists():
    assert Queue


# @pytest.mark.skip("TODO")
# Can successfully instantiate an empty queue
def test_enqueue():
    q = Queue()
    q.enqueue("apple")
    actual = q.front.value
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully dequeue out of a queue the expected value
def test_dequeue():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    actual = q.dequeue()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully peek into a queue, seeing the expected value
def test_peek():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    actual = q.peek()
    expected = "apple"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Calling peek on empty queue raises exception
def test_peek_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.peek()


# @pytest.mark.skip("TODO")
# Can successfully enqueue into a queue
def test_enqueue_one():
    q = Queue()
    q.enqueue("apples")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully enqueue multiple values into a queue
def test_enqueue_two():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.peek()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
# Calling dequeue on empty queue raises exception
def test_dequeue_when_empty():
    q = Queue()
    with pytest.raises(InvalidOperationError):
        q.dequeue()


# @pytest.mark.skip("TODO")
def test_dequeue_when_full():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    actual = q.dequeue()
    expected = "apples"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_peek_post_dequeue():
    q = Queue()
    q.enqueue("apples")
    q.enqueue("bananas")
    q.dequeue()
    actual = q.peek()
    expected = "bananas"
    assert actual == expected


# @pytest.mark.skip("TODO")
def test_is_empty():
    q = Queue()
    actual = q.is_empty()
    expected = True
    assert actual == expected


# @pytest.mark.skip("TODO")
# Can successfully empty a queue after multiple dequeues
def test_exhausted():
    q = Queue()
    q.enqueue("apple")
    q.enqueue("banana")
    q.enqueue("cucumber")
    q.dequeue()
    q.dequeue()
    q.dequeue()
    actual = q.is_empty()
    expected = True
    assert actual == expected
