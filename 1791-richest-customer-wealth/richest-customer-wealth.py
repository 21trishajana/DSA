class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        maxWealth = 0
        for i in range(len(accounts)):
            currWealth = sum(accounts[i])
            maxWealth = max(maxWealth,currWealth)
        return maxWealth