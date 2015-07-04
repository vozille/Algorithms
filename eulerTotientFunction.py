phi = [0]*11
n = 10
for i in range(1,n+1):
    phi[i] += i
    for j in range(2*i,n+1,i):
        phi[j] -= phi[i]
print phi
