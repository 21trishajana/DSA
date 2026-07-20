class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pc = {}
        sc = {}
        left = 0
        ans = []
        for i in range(len(p)):
            pc[p[i]] = pc.get(p[i], 0) + 1
        
        for right in range(len(s)):
            sc[s[right]] = sc.get(s[right], 0) + 1
            if right - left + 1 == len(p):
                if pc == sc:
                    ans.append(left)
                sc[s[left]] -= 1
                if sc[s[left]] == 0:
                    del sc[s[left]]
                left += 1
        return ans