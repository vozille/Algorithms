mod = 10**9+7
factorial = [1 for i in range(1000)]
ifactorial = [1 for i in range(1000)]

def nCr(n,r):
    res = 1
    res = res*factorial[n]%mod
    res = res*ifactorial[r]%mod
    res = res*ifactorial[n-r]%mod
    return res

def fill():
    for i in range(1,1000):
        factorial[i] = i*factorial[i-1]%mod
        ifactorial[i] = pow(factorial[i],(mod-2),mod)%mod
fill()

print nCr(50,3)
