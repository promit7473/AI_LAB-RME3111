from collections import deque

# Initialize a deque as a queue
queue = deque()

# Enqueue operation
queue.append(10)
queue.append(20)
queue.append(30)

print("Queue after enqueueing:", queue)  # Output: deque([10, 20, 30])

# Dequeue operation
dequeued_value = queue.popleft()  # Removes and returns the first element
print("Dequeued:", dequeued_value)  # Output: 10

# Print the queue after dequeue
print("Queue after dequeue:", queue)  # Output: deque([20, 30])

# Check if queue is empty
is_empty = len(queue) == 0
print("Is the queue empty?", is_empty)  # Output: False

print("The final state of the queue is", list(queue))