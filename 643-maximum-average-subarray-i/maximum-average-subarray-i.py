class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left = 0
        ans = 0
        anss = float("-inf")
        for right in range(len(nums)):
            ans += nums[right]
            if right - left + 1 == k:
                anss = max(anss, ans/k)
                ans -= nums[left]
                left += 1
        return anss