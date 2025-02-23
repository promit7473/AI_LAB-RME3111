# Max Heap Implementation

def reheap_down_max(heap, index, size):
    """
    Ensures the max heap property is maintained when moving down the heap.
    """
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    largest = index

    # Check if the left child exists and is greater than the current largest
    if left_child < size and heap[left_child] > heap[largest]:
        largest = left_child

    # Check if the right child exists and is greater than the current largest
    if right_child < size and heap[right_child] > heap[largest]:
        largest = right_child

    # If the largest is not the current index, swap and continue reheap_down
    if largest != index:
        heap[index], heap[largest] = heap[largest], heap[index]
        reheap_down_max(heap, largest, size)


def reheap_up_max(heap, index):
    """
    Ensures the max heap property is maintained when moving up the heap.
    """
    parent = (index - 1) // 2
    if index > 0 and heap[index] > heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]
        reheap_up_max(heap, parent)


# Example Usage for Max Heap
if __name__ == "__main__":
    # Initial array representing the max heap
    # Max Heap Tree (Before Reheap Down):
    #
    #         3
    #        / \
    #       7   6
    #      / \   \
    #     5   4   9
    #
    heap = [3, 7, 6, 5, 4, 9]

    print("Before Reheap Down:", heap)
    reheap_down_max(heap, 0, len(heap))  # Fix the heap property starting from the root
    print("After Reheap Down:", heap)

    # Max Heap Tree (After Reheap Down):
    #
    #         9
    #        / \
    #       7   6
    #      / \   \
    #     5   4   3