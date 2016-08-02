def zFunction(s):
    left,right,n = 0,0,len(s)
    z = [0]*n
    for i in range(1,n):
        if i <= right:
            z[i] = min(right-i+1,z[i-left])
        while i+z[i] < n and s[z[i]] == s[i+z[i]]:
            z[i] += 1
        if i+z[i]-1 > right:
            left = i
            right = i+z[i]-1
    return z
