def binarySearch(s,x):
    low,high = 0,len(s)
    mid = (high+low)/2
    while low < high:
        if s[mid] == x:
            return mid
        if s[mid] > x:
            high = mid
        else:
            low = mid+1
        mid = (high+low)/2
    return -1
