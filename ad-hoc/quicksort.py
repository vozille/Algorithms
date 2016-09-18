def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    i += 1
    arr[i], arr[high] = arr[high], arr[i]
    return i

def quicksort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        print p
        quicksort(arr, low, p - 1)
        quicksort(arr, p + 1, high)

arr = [1, 5 ,2 ,4 ,3 , -5]
n = len(arr) - 1
quicksort(arr, 0, n)
print arr
