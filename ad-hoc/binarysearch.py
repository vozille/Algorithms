def binarySearch(arr, num):
    # zero based index
    low,high = 0,len(arr)
    mid = (high+low)/2
    while low < high:
        if arr[mid] == num:
            return mid
        if arr[mid] > num:
            high = mid
        else:
            low = mid+1
        mid = (high+low)/2
    return -1

arr = [10, 20, 30, 40, 50, 60, 70]
print binarySearch(arr, 20)
