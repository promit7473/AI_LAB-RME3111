from collections import deque

def max_heap_down(heap, index):
    size = len(heap)
    dq = deque([index])  #index of the root

    while dq:
        current_index = dq.popleft()
        left_child = 2 * current_index + 1
        right_child = 2 * current_index + 2
        largest = current_index

        # Comparing with left child
        if left_child < size and heap[left_child] > heap[largest]:
            largest = left_child

        # Comparing with right child
        if right_child < size and heap[right_child] > heap[largest]:
            largest = right_child

        # If the largest is not the current index, swap and continue down
        if largest != current_index:
            heap[current_index], heap[largest] = heap[largest], heap[current_index]
            dq.append(largest)

# Example usage
heap = [1, 3, 4, 9, 11, 7, 8, 6]  # Sample min-heap
print("Original Heap:", heap)

# Perform max heap down on the root
max_heap_down(heap, 0)

print("Heap after max heap down:", heap)
