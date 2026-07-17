class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        hset = set()
        ans = []
        for i in nums:
            if i in hset:
                ans.append(i)
            hset.add(i)
        return ans