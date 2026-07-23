class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        first = strs[0]
        for i in range(len(first)):
            for word in strs:
                if i >=  len(word) or word[i] != first[i]:
                    return res

            res += first[i]

        return res                