"""
Given two arrays with same elements,
find the minimum number of swaps to convert one to the other

say [1, 2, 3] and [3, 1, 2] requires 2 swaps
"""
def merge_and_count(a, b):
    assert a == sorted(a) and b == sorted(b)
    c = []
    count = 0
    i, j = 0, 0
    while i < len(a) and j < len(b):
        c.append(min(b[j], a[i]))
        if b[j] < a[i]:
            count += len(a) - i
            j+=1
        else:
            i+=1
    # now we reached the end of one the lists
    c += a[i:] + b[j:] # append the remainder of the list to C
    return count, c

def sort_and_count(L):
    if len(L) == 1: return 0, L
    n = len(L)/ 2
    a, b = L[:n], L[n:]
    ra, a = sort_and_count(a)
    rb, b = sort_and_count(b)
    r, L = merge_and_count(a, b)
    return ra+rb+r, L

def get_permutation(L1, L2):
    if sorted(L1) != sorted(L2):
        raise ValueError("L2 must be permutation of L1 (%s, %s)" % (L1,L2))

    permutation = map(dict((v, i) for i, v in enumerate(L1)).get, L2)
    assert [L1[p] for p in permutation] == L2
    return permutation

def number_of_swaps(permutation):

    nswaps = 0
    seen = set()
    for i in xrange(len(permutation)):
        if i not in seen:
            j = i
            while permutation[j] != i:
                j = permutation[j]
                seen.add(j)
                nswaps += 1
    return nswaps

a = [1, 2, 3]
b = [3, 1, 2]

print number_of_swaps(get_permutation(a,b))
