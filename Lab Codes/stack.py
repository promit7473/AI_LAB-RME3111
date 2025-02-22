# stack.py

class Stack:
    def __init__(self, size):
        self.stack = [0] * size
        self.top = -1

    def push(self, n):
        if self.top < len(self.stack) - 1:  # Checking if the stack is not full
            self.top += 1
            self.stack[self.top] = n
        else:
            print("Stack Overflow")

    def pop(self):
        if self.top >= 0:  # Checking if the stack is not empty
            popped_value = self.stack[self.top]
            self.top -= 1
            return popped_value
        else:
            print("Stack Underflow")
            return None

    def is_empty(self):
        return self.top == -1
