def binary_search(arr, target):
    """
    Function to perform binary search on a sorted array.
    :param arr: Sorted list of elements
    :param target: Element to search for
    :return: Index of the target if found, otherwise -1
    """
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  # Calculate the middle index
        print(f"Low = {low}, High = {high}, Mid = {mid} (Value = {arr[mid]})")

        if arr[mid] == target:
            print("-> Found!")
            return mid  # Target found at index `mid`
        elif arr[mid] < target:
            low = mid + 1  # Search in the right half
        else:
            high = mid - 1  # Search in the left half

    print("-> Not Found!")
    return -1  # Target not found


# Example Usage for Binary Search
if __name__ == "__main__":
    # Initial sorted array
    # ASCII Diagram of Binary Search
    #
    # Array: [1, 3, 5, 7, 9, 11]
    # Target: 7
    #
    # Step-by-Step Process:
    # Step 1: Low = 0, High = 5, Mid = 2 (Value = 5)
    # Step 2: Low = 3, High = 5, Mid = 4 (Value = 9)
    # Step 3: Low = 3, High = 3, Mid = 3 (Value = 7) -> Found!
    #
    arr = [1, 3, 5, 7, 9, 11]
    target = 7

    print("Performing Binary Search:")
    result = binary_search(arr, target)

    if result != -1:
        print(f"Target {target} found at index {result}.")
    else:
        print(f"Target {target} not found in the array.")