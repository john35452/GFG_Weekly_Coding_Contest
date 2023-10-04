#User function Template for python3

class Solution:
    # Version 1: Unique character count
    # TC: O(n), SC: O(1)
    def solve(self, N, S):
        from collections import Counter
        fre = Counter(S)
        return len(fre) - 1