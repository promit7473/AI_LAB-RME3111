# Min Heap Implementation

def reheap_down_min(heap, index, size):
    """
    Ensures the min heap property is maintained when moving down the heap.
    """
    left_child = 2 * index + 1
    right_child = 2 * index + 2
    smallest = index

    # Check if the left child exists and is smaller than the current smallest
    if left_child < size and heap[left_child] < heap[smallest]:
        smallest = left_child

    # Check if the right child exists and is smaller than the current smallest
    if right_child < size and heap[right_child] < heap[smallest]:
        smallest = right_child

    # If the smallest is not the current index, swap and continue reheap_down
    if smallest != index:
        heap[index], heap[smallest] = heap[smallest], heap[index]
        reheap_down_min(heap, smallest, size)


def reheap_up_min(heap, index):
    """
    Ensures the min heap property is maintained when moving up the heap.
    """
    parent = (index - 1) // 2
    if index > 0 and heap[index] < heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]
        reheap_up_min(heap, parent)


# Example Usage for Min Heap
if __name__ == "__main__":
    # Initial array representing the min heap
    # Min Heap Tree (Before Reheap Up):
    #
    #         9
    #        / \
    #       7   6
    #      / \   \
    #     5   4   3
    #
    heap = [9, 7, 6, 5, 4, 3]

    print("Before Reheap Up:", heap)
    reheap_up_min(heap, len(heap) - 1)  # Fix the heap property starting from the last element
    print("After Reheap Up:", heap)

    # Min Heap Tree (After Reheap Up):
    #
    #         3
    #        / \
    #       7   6
    #      / \   \
    #     5   4   9