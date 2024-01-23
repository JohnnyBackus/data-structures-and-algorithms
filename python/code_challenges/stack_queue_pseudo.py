from data_structures.stack import Stack


class PseudoQueue:
    def __init__(self):
        self.enqueue_stack = Stack()
        self.dequeue_stack = Stack()

    def enqueue(self, value):
        enqueue_stack = self.enqueue_stack
        dequeue_stack = self.dequeue_stack
        while dequeue_stack.top is not None:
            enqueue_stack.push(dequeue_stack.pop())
        enqueue_stack.push(value)

    def dequeue(self):
        enqueue_stack = self.enqueue_stack
        dequeue_stack = self.dequeue_stack
        while enqueue_stack.top is not None:
            dequeue_stack.push(enqueue_stack.pop())
        return dequeue_stack.pop()
