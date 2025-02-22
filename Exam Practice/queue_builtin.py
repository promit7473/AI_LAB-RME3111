from collections import deque

# Initialize a deque as a queue
queue = deque()

# Enqueue operation
queue.append(10)
queue.append(20)

# Dequeue operation
dequeued_value = queue.popleft()  # Removes and returns the first element
print(dequeued_value)  # Output: 10

# Check if queue is empty
is_empty = len(queue) == 0

