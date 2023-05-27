from typing import List


class Solution:
    # Version 1: Binary Search
    # Since 2^k can contribute more within 10^9, 
    # We can search for the greatest valid k.
    # TC: O(logn), SC: O(1)
    '''
    def checkIfPossible(self, n : int) -> List[int]:
        # code here
        def check(val):
            return 2 ** val <= maxv and val <= n
            
        maxv = 10 ** 9
        l = 0
        r = n
        while l < r:
            m = l + (r - l) // 2
            if not check(m):
                r = m
            else:
                l = m + 1
        if not check(l):
            l -= 1
        if l == n:
            return [2**l, 1]
        elif 3 ** (n - l) <= maxv:
            return [2**l, 3 ** (n - l)]
        else:
            return [-1]
    '''
    
    # Version 2: Check all combination
    # TC: O(n), SC: O(1)
    def checkIfPossible(self, n : int) -> List[int]:
        maxv = 10 ** 9
        for i in range(n + 1):
            if 2 ** i <= maxv and 3 ** (n - i) <= maxv:
                return [2 ** i, 3 ** (n - i)]
        return [-1]
                
