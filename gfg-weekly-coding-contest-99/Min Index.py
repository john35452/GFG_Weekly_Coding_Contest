from typing import List


class Solution:
    # Version 1: Count the frequency
    # TC: O(n), SC: O(n)
    def minIndex(self, n : int, arr : List[int]) -> int:
        # code here
        from collections import Counter
        res = [0]*n
        fre = Counter(arr)
        for i in range(n):
           res[i] = fre[arr[i] * 2] + fre[arr[i] * 3] + fre[arr[i] * 4] + fre[arr[i] * 5]
        return res.index(max(res))