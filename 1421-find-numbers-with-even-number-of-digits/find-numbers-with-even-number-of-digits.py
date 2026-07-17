class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for nums in nums:
            temp = nums
            digit = 0
            while temp > 0:
                temp = temp // 10
                digit += 1
            if digit % 2 == 0:
                count += 1
        return count
