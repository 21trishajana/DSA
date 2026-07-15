class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, no in enumerate(nums):
            compliment = target - no
         
            if compliment in seen:
                return [seen[compliment],i]
            
            seen[no] = i

                