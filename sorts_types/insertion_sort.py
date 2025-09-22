# Comments
import random


def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
            arr[j + 1] = key
        return arr
    return None


arr = [64,34,25,12,22,11,90,88,79,65,23,55,81]
print(insertion_sort(arr))