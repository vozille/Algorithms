import operator

s = [[1,2,3],[5,1,7],[3,0,9]]
k = 1
s = sorted(s, key=operator.itemgetter(k))
for i in s:
    for j in i:
        print j,
    print ''
