from typing import List


class Solution:
    # Version 1: Sort
    # TC: O(nlogn), SC: O(n)
    def dominantPairs(self, n : int, arr : List[int]) -> int:
        # code here
        half = n // 2
        left = arr[:half]
        right = arr[half:]
        left.sort()
        right.sort()
        ans = 0
        i = 0
        for j in range(len(right)):
            while i < half and left[i] < 5*right[j]:
                i += 1
            ans += (half - i)
        return ans

