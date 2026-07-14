class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        seen = {0:1}
        prefixsum = 0
        count = 0
        for i in range(len(nums)):
            prefixsum += nums[i]
            if prefixsum - k in seen:
                count += seen[prefixsum - k]
        
            if prefixsum in seen:
                seen[prefixsum] += 1
            else:
                seen[prefixsum] = 1
        return count
