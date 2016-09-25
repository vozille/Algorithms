def kmp(pattern,string):
    shifts = [1]*(len(pattern)+1)
    val = 1
    for i in range(len(pattern)):
        while val <= i and pattern[i] != pattern[i-val]:
            val += shifts[i-val]
        shifts[i+1] = val

    start = 0
    match = 0
    for i in range(len(string)):
        while match == len(pattern) or match >= 0 and pattern[match] != string[i]:
            start += shifts[match]
            match -= shifts[match]
        match += 1
        if match == len(pattern):
            yield start

a = 'abcdabcdjhjldgflhglhljfhaljehabcd'
p = 'abcd'
ans = list(kmp(p,a))
print ans
