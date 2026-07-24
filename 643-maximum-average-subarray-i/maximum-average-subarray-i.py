class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = 0
        sum = 0
        maxavg = float("-inf")
        for r in range(len(nums)):
            sum += nums[r]
            if r - l + 1 == k:
                maxavg = max(maxavg, sum / k)
                sum -= nums[l]
                l += 1
        return maxavg