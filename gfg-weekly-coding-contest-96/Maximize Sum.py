#User function Template for python3

class Solution:
    # Version 1: Sort
    # The bigger value should have bigger weight.
    # TC: O(nlogn), SC: O(1)
    def maximumSum(self, n, A):
        # code here
        A.sort()
        ans = 0
        for i in range(n):
            ans += (i + 1)*A[i]
        return ans