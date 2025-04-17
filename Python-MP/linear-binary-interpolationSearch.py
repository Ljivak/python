import random
import time
from typing import Tuple



def linear_search(array, local_target: int):

    for i in range(0, len(array)):
       if array[i] == local_target:
            return i
    return -1

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

def time_measure(func) -> Tuple[float, int]:

    start_time = time.perf_counter()
    result = func()
    end_time = time.perf_counter()
    return end_time - start_time, result

def prepare_arr1(elements_num: int, value_limitation: int):
    array = [random.randint(1, value_limitation) for _ in range(elements_num)]
    array.sort()
    return array

def prepare_arr2(elements_num: int):
    array = list(range(1, elements_num + 1))
    for i in range(elements_num):
        array[i] += random.randint(-2, 2)
    array.sort()
    return array

n = 200000 #number of elements in the array
m = 60000
target = 5000
runs = 3

print("for array 1:")
for run in range(runs):

    arr1 = prepare_arr1(n, m)
    lineartime, linearplace = time_measure(lambda: linear_search(arr1, target))
    binarytime, binaryplace = time_measure(lambda: binary_search(arr1, target))
    print(f"array 1, target={target}, run N={run}, linear search time={lineartime:.8f}s, linear result={linearplace}")
    print(f"array 1, target={target}, run N={run}, binary search time={binarytime:.8f}s, binary result={binaryplace}")

print("for array 2:")
#linear result oraz binary result will be almost the same because of the design of the array 2
for run in range(runs):

    arr2 = prepare_arr2(n)
    lineartime, linearplace = time_measure(lambda: linear_search(arr2, target))
    binarytime, binaryplace = time_measure(lambda: binary_search(arr2, target))
    print(f"array 2, target={target}, run N={run}, linear search time={lineartime:.8f}s, linear result={linearplace}")
    print(f"array 2, target={target}, run N={run}, binary search time={binarytime:.8f}s, binary result={binaryplace}")

print("for interpolation search:")
for run in range(runs):

    arr2 = prepare_arr2(n)
    arr1 = prepare_arr1(n, m)
    lineartime1, linearplace1 = time_measure(lambda: linear_search(arr1, target))
    lineartime2, linearplace2 = time_measure(lambda: linear_search(arr2, target))
    interpolationtime1, interpolationplace1 = time_measure(lambda: interpolation_search(arr1, target))
    interpolationtime2, interpolationplace2 = time_measure(lambda: interpolation_search(arr2, target))
    print(f"array 1, target={target}, run N={run}, interpolation search time={interpolationtime1:.8f}s, interpolation result={interpolationplace1}")
    print(f"array 1, target={target}, run N={run},        linear search time={lineartime1:.8f}s, linear result={linearplace1}")
    print(f"array 2, target={target}, run N={run}, interpolation search time={interpolationtime2:.8f}s, interpolation result={interpolationplace2}")
    print(f"array 2, target={target}, run N={run},        linear search time={lineartime2:.8f}s, linear result={linearplace2}")

"""
pesymistyczny przypadek wyszukiwania interpolacyjnego - to może być tablica gdzie dane są nierównomiernie rozłożone. Na przykład wszystkie liczby są duże oprócz pierwszej. {1,199,200,200,200,200,200}. Wtedy formuła dla target=199:  pos = 0 + (199 - 1)*(6 - 0)//(200 - 1) = 5, 
następnie pos =  0 + (199 - 1)*(5 - 0)//(200 - 1) = 4, i tak dalej. W takim przypadku złożoność wyszukiwania jest O(n) czyli taka sama jak w linear search.
"""