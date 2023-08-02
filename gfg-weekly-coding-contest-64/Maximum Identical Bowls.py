
from typing import List
class Solution:
    # Version 1: Find the maximum divisor of sum(arr)
    # TC: O(n), SC: O(1)
    def getMaximum(self, N : int, arr : List[int]) -> int:
        # code here
        total = sum(arr)
        ans = N
        while total % ans > 0:
            ans -= 1
        return ans

