# Time complexity - O(n) (plus O(365) # creating array with length equal to last number 
# in days array which can be max 365)
# Space complexity - O(365) i.e. O(1)

# Approach - Create a dp array with length equal to last value in days array, for 
# every index in dp, compute the minimum value for ticket considering the index is
# in-bounds. 

from typing import List
class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0 for i in range(days[-1]+1)]
        hashset = set()

        for d in days:
            if d not in hashset:
                hashset.add(d)
        
        for i in range(days[-1]+1):
            if i not in hashset:
                dp[i] = dp[i-1]
            else:
                if i < 7:
                    dp[i] = min(dp[i-1] + costs[0], dp[0] + costs[1], dp[0] + costs[2])
                elif i < 30:
                    dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[0] + costs[2])
                else:
                    dp[i] = min(dp[i-1] + costs[0], dp[i-7] + costs[1], dp[i-30] + costs[2])
        print(hashset) 
        print(dp)
        return dp[-1]