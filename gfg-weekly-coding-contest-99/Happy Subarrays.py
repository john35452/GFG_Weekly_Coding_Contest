from typing import List


class Solution:
    # Version 1: Prefix XOR
    # Perfect subarray is a subarray with zero xor result.
    # TC: O(n), SC: O(n)
    def happySub(self, n : int, arr : List[int]) -> int:
        # code here
        M = 10 ** 9 + 7
        xor = {0: 1}
        current = 0
        ans = 0
        for val in arr:
            current ^= val
            if current in xor:
                ans = (ans + xor[current]) % M
            else:
                xor[current] = 0
            xor[current] += 1
        return ans
