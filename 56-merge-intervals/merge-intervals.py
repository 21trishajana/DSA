class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        sort = sorted(intervals,key=lambda x:x[0])
        merged = []
        for i in sort:
            if not merged:
                merged.append(i)
            else:
                if merged[-1][1] >= i[0]:
                    merged[-1][1] = max(merged[-1][1], i[1])
                else:
                    merged.append(i)
        return merged