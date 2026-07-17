class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        seen = {}
        for i, no in enumerate(nums):
            
            if no in seen:
                if i - seen[no] <= k:
                    return True
            seen[no] = i
        return False
