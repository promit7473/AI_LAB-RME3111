def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i

        for j in range(i+1,len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[min_index],arr[i] = arr[i],arr[min_index]

    return arr

if __name__ == '__main__':
    my_array = [9, 2, 6, 5, 3]
    print(selection_sort(my_array))