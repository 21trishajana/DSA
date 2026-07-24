class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        minsub = float("inf")
        l = 0
        sum = 0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                minsub = min(minsub, r - l + 1)
                sum -= nums[l]
                l += 1
        return 0 if minsub == float("inf") else minsub