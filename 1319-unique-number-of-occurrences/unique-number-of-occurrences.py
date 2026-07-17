class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        seen = {}
        for i in arr:
            seen[i] = seen.get(i,0) + 1
        
        occurences = set()
        for j in seen.values():
            if j in occurences:
                return False
            occurences.add(j)
        return True

