class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        j,ans = 0,0
        for i in range(len(s)):
            while s[i] in seen:
                seen.remove(s[j])
                j += 1
            seen.add(s[i])
            ans = max(ans, i - j + 1)
        return ans