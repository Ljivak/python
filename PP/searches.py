
# linear search. Time complexity O(1) - O(n).  
def linear_search(array, local_target: int):

    for i in range(0, len(array)):
       if array[i] == local_target:
            return i
    return -1



# binary search. Time complexity O(1) - O(log n).
def binary_search(array, local_target: int):

    low, high = 0, len(array) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if array[mid] == local_target:
            return mid

        elif array[mid] < local_target:
            low = mid + 1

        else:
            high = mid - 1

    return -1



# interpolation search. Time complexity O(1) - O( log(log n) ).
def interpolation_search(array, local_target: int):

    low, high = 0, len(array) - 1
    while array[low] <= array[high] and array[low] <= local_target <= array[high]:
        if array[low] == array[high]:
            if array[low] == local_target:
                return low
            return -1

        pos = min([len(array) - 1, (low + (((high - low) * (local_target - array[low])) // (array[high] - array[low])))])

        if array[pos] == local_target:
            return pos

        elif array[pos] < local_target:
            low = pos + 1

        else:
            high = pos - 1

    return -1
