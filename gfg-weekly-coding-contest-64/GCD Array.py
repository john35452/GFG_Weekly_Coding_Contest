

from typing import List
class Solution:
    # Version 1: GCD
    # si can be divided by G, which means sum(si) also can be divided by G
    # Therefore, we can find the answer from the divisor of sum(arr)
    # Since it will be divided into K group, when there are more than K prefix sum can be divided by a number.
    # It means that number is a option among G.
    # TC: O(n * sqrt(sum(arr))), SC: O(1)
    def solve(self, N : int, K : int, arr : List[int]) -> int:
        # code here
        import math
        def check(val):
            res = 0
            for v in arr:
                res += int(v % val == 0)
            return res >= K
        
        for i in range(1, N):
            arr[i] += arr[i - 1]
        total = arr[-1]
        ans = 0
        for i in range(1, int(math.sqrt(total)) + 1):
            if total % i == 0:
                if check(total // i):
                    ans = max(ans, total // i)
                    break
                if check(i):
                    ans = max(ans, i)
        return ans
        