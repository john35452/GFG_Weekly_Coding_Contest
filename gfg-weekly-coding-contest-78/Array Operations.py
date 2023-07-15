from typing import List


class Solution:
    # Version 1: Greedy
    # We can make any subarray without zero to all zero with one operation.
    # Therefore, we can count the number of longest non-zero subarrays.
    # However, we always can do one things.
    # Choose the whole array, and set them all to MEX
    # Then choose the whole array again to set them to 0.
    # Therefore, we can always make it to 0 with at most 2 operations.
    # TC: O(n), SC: O(1)
    def arrayOperations(self, n : int, arr : List[int]) -> int:
        # code here
        ans = 0
        l = 0
        for i in range(n):
            if arr[i] == 0:
                if i > l:
                    ans += 1
                l = i + 1
        if l < n:
            ans += 1
        return min(ans, 2)

