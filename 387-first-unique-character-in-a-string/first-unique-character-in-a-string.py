class Solution:
    def firstUniqChar(self, s: str) -> int:
        seen = {}
        for i in s:
            seen[i] = seen.get(i,0) + 1
        for i, ch in enumerate(s):
            if seen[ch] == 1:
                return i
        return -1