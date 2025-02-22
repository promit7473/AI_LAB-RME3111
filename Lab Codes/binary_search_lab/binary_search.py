def binary_search(arr, low, high, target):
    while low <= high:
        mid = (low + high) >> 1

        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1

if __name__ == '__main__':
    my_list = [1, 3, 5, 7, 7, 9]
    my_target = 7
    search = binary_search(my_list, 0, len(my_list) - 1, my_target)
    if search == -1:
        print("The item is not in the list")
    else:
        print(f"The item is in the list and the position is {search}")
