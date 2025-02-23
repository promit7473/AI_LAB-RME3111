from collections import deque

# Max Heap Up (Used for Insertion)
def max_heap_up(heap, index):
    parent = (index - 1) // 2
    if index > 0 and heap[index] > heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]  # Swap with parent
        max_heap_up(heap, parent)  # Recursive call

# Insert (Enqueue) a value into the heap
def enqueue(heap, value):
    heap.append(value)  # Add at the end
    max_heap_up(heap, len(heap) - 1)  # Fix heap

# Max Heap Down (Used for Deletion)
def max_heap_down(heap, index):
    size = len(heap)
    dq = deque([index])  # Start from root

    while dq:
        current_index = dq.popleft()
        left_child = 2 * current_index + 1
        right_child = 2 * current_index + 2
        largest = current_index

        # Compare with left child
        if left_child < size and heap[left_child] > heap[largest]:
            largest = left_child

        # Compare with right child
        if right_child < size and heap[right_child] > heap[largest]:
            largest = right_child

        # If the largest is not the current index, swap and continue
        if largest != current_index:
            heap[current_index], heap[largest] = heap[largest], heap[current_index]
            dq.append(largest)

# Remove the maximum element (Dequeue)
def dequeue(heap):
    if len(heap) == 0:
        return None  # Heap is empty

    max_value = heap[0]  # Root (max value)
    heap[0] = heap[-1]  # Replace root with last element
    heap.pop()  # Remove last element
    max_heap_down(heap, 0)  # Fix heap

    return max_value  # Return the removed max value

# Example Usage
heap = [10, 9, 5, 7, 6, 2, 1]  # Initial Max Heap

print("Initial Heap:", heap)

# Insert a value
enqueue(heap, 11)
print("Heap after inserting 11:", heap)

# Remove the maximum value (root)
removed_value = dequeue(heap)
print(f"Removed Max Value: {removed_value}")
print("Heap after deletion:", heap)
