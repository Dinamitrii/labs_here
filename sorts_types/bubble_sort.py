# Comments like that

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

if __name__ == '__main__':
    arr = [64,34,25,12,22,11,90,88,48,67,92]
    print(bubble_sort(arr))