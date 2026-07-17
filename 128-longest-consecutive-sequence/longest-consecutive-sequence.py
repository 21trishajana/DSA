class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hset = set(nums)
        longest = 0
        
        for num in hset:
            if num - 1 not in hset:
                start = num
                count = 1
            
                while start + 1 in hset:
                    count += 1
                    start += 1
                longest = max(longest,count)

        return longest
