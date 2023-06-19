
from typing import List


class Solution:
    # Version 1: Use prefix to calculate cost for each index
    # Let say index is 1.
    # The cost is arr[0] * 1 + arr[1] * 0 + arr[2] * 1 + ...+ arr[n - 1] * (n - 2)
    # The cost for index 2 is as below.
    # arr[0] * 2 + arr[1] * 1 + arr[2] * 0 + arr[3] * 1 + ...+ arr[n - 1] * (n - 3)
    # The difference is (arr[0] + arr[1]) - (arr[2] + arr[3] + ... + arr[n - 1])
    # Therefore, we can use prefix sum to adjust from one index to another.
    # TC: O(n), SC: O(n)
    def gatheringCost(self, N : int, weightsArr : List[int]) -> int:
        # code here
        prefix = [0]*(N + 1)
        current = 0
        for i in range(N):
            prefix[i + 1] = prefix[i] + weightsArr[i]
            current += i * (weightsArr[i])
        
        ans = current
        for i in range(N):
            current += prefix[i + 1]
            current -= prefix[N] - prefix[i + 1]
            ans = min(ans, current)
        return ans
        