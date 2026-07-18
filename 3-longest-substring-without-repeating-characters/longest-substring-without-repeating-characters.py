class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hset = set()
        l,ans = 0,0
        for r in range(len(s)):
            while s[r] in hset:
                hset.remove(s[l])
                l += 1
            hset.add(s[r])
            ans = max(ans,r-l+1)
        return ans