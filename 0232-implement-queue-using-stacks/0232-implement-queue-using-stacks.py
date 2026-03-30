class MyQueue:

    def __init__(self):
        self.stack_in = []
        self.stack_out = []

    def push(self, x: int) -> None:
        # Always push to the input stack
        self.stack_in.append(x)

    def pop(self) -> int:
        # Ensure stack_out has the current FIFO elements
        self.peek()
        return self.stack_out.pop()

    def peek(self) -> int:
        # If stack_out is empty, move all elements from stack_in
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())
        return self.stack_out[-1]

    def empty(self) -> bool:
        # The queue is empty only if both stacks are empty
        return not self.stack_in and not self.stack_out