def reheap_down(heap, index, size):
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    smallest = index

    # Comparing with left child
    if left_child < size and heap[left_child] < heap[smallest]:
        smallest = left_child

    # Comparing with right child
    if right_child < size and heap[right_child] < heap[smallest]:
        smallest = right_child

    # If the smallest is not the current index, swap and continue reheap down
    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        reheap_down(heap, smallest, size)

heap1 = [11, 9, 4, 3, 1, 7, 8, 6]

# Perform reheap down starting from the root
reheap_down(heap1, 0, len(heap1))

print("Heap after reheap down:", heap1)
