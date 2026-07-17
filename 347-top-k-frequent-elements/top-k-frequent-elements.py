class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        seen = {}
        for i in nums:
            seen[i] = seen.get(i,0) + 1
        sort = sorted(seen.items(), key = lambda x: x[1], reverse = True)
        result = []
        for nums,freq in sort[:k]:
            result.append(nums)

        return result