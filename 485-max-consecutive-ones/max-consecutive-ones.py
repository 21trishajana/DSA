class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes = 0
        curSum = 0
        for i in nums:
            
            if i == 0:
                curSum = 0
            else:
                curSum += 1
            maxOnes = max(maxOnes,curSum)
        return maxOnes