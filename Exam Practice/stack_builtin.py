# Using Python's built-in list as a stack
stack = []

# Push operation
stack.append(10)
stack.append(20)
stack.append(38)

# Pop operation
popped_value = stack.pop()  # Removes and returns the last element
print(popped_value)  # Output: 20

# Check if stack is empty
is_empty = len(stack) == 0
print(is_empty)
print(stack)