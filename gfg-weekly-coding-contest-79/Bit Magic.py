from typing import List


class Solution:
    # Version 1: Greedy
    # For each pair of mismatch, there is one 1 and 0.
    # We make every two 1 into 0 with one operation
    # Also one operation to make one 1 and 0 to two 0.
    # TC: O(n), SC: O(1)
    def bitMagic(self, n : int, arr : List[int]) -> int:
        # code here
        mismatch = 0
        for i in range(n // 2):
            if arr[i] != arr[n - 1 -i]:
                mismatch += 1
        return mismatch // 2 + mismatch % 2