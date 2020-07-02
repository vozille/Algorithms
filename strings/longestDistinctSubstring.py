class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = set()
        max_length = 0
        i, j = 0, 0
        while i < len(s) and j < len(s):
            if s[j] not in visited:
                visited.add(s[j])
                j += 1
                max_length = max(max_length, abs(j - i))
            else:
                visited.remove(s[i])
                i += 1
        return max_length
