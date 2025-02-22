def max_heap_sort(heap, index):
    last_index = index


    if index > 0 and heap[] > heap[last_index]:
        heap[index], heap[last_index] = heap[last_index], heap[index]  # Swap with parent
        max_heap_sort(heap, last_index) #using recursion

#simple enqueue function
def enqueue(onno, value):
    onno.append(value)
    max_heap_sort(heap, len(heap) - 1)


heap = [1, 3, 4, 9, 11]
onno = []
print("Original Heap:", heap)

new_value = heap[len(heap)-1]
enqueue(onno, new_value)

print("Heap short", onno)
