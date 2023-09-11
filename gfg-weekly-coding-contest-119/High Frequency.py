#User function Template for python3

class Solution:
    # Version 1: Most frequent character
    # TC: O(n), SC: O(26) = O(1)
    def solve(self,N,S):
        #code here
        from collections import Counter
        fre = Counter(S)
        count = 0
        ans = None
        for k, v in fre.items():
            if v > count:
                ans = k
                count = v
            elif v == count and k < ans:
                ans = k
        return ans



