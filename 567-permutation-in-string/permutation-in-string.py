class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need = {}
        window = {}
        j = 0
        for i in range(len(s1)):
            need[s1[i]] = need.get(s1[i], 0) + 1
        for i in range(len(s2)):
            window[s2[i]] = window.get(s2[i], 0) + 1
            if i - j + 1 == len(s1):
                if need == window:
                    return True
                window[s2[j]] -= 1
                if window[s2[j]] == 0:
                    del window[s2[j]]
                j += 1
        return False