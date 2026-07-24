class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1d= {}
        for i in range(len(s1)):
            s1d[s1[i]] = s1d.get(s1[i], 0) + 1
        s2d ={}
        l = 0
        for i in range(len(s2)):
            s2d[s2[i]] = s2d.get(s2[i], 0) + 1
            if i - l + 1 == len(s1):
                if s1d == s2d:
                    return True
                s2d[s2[l]] -= 1
                if s2d[s2[l]] == 0:
                   del s2d[s2[l]]
                l += 1
        return False