# worst case implementation O(n^2 log(n)) x O(m*n)
for _ in range(input()):
    s = raw_input()
    d = {}
    substr = []
    for i in range(len(s)):
        substr.append(s[i:len(s)])
        d[s[i:len(s)]] = i+1
    substr.sort()

    def get_lcp(a,b):
        ans = 0
        for i in range(len(a)):
            if a[i] != b[i]:
                return ans
            ans += 1
        return ans

    res = 1

    for i in range(len(substr)-1):
        res += len(substr[i+1]) - get_lcp(substr[i],substr[i+1])
    print res
