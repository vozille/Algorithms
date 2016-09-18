import operator
from operator import *
m,n = map(int,raw_input().split())
s = []
for i in range(m):
    foo = map(int,raw_input().split())
    s.append(foo)
k = input()
s = sorted(s, key=operator.itemgetter(k))
for i in range(m):
    for j in s[i]:
        print j,
    print ''
