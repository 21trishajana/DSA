class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s = len(s1)
        left = 0
        s1_count = {}
        for i in range(s):
            s1_count[s1[i]] = s1_count.get(s1[i],0) + 1
        curr_count = {}
        for right in range(len(s2)):
            curr_count[s2[right]] = curr_count.get(s2[right],0) + 1
            if right - left + 1 == s:
                if s1_count == curr_count:
                    return True
                
                curr_count[s2[left]] -= 1
                if curr_count[s2[left]] == 0:
                    del curr_count[s2[left]]
                left += 1
        return False

