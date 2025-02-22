def min_heap_up(heap, index):
    parent = (index - 1) // 2


    if index > 0 and heap[index] < heap[parent]:
        heap[index], heap[parent] = heap[parent], heap[index]  # Swap with parent
        min_heap_up(heap, parent) #using recursion

#simple enqueue function
def enqueue(heap, value):
    heap.append(value)
    min_heap_up(heap, len(heap) - 1)


heap = [1, 3, 4, 9, 11, 7, 8, 6]
print("Original Heap:", heap)

new_value = 2
enqueue(heap, new_value)

print("Heap after enqueue and min heap up:", heap)
