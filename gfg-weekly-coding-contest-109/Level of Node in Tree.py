#User function Template for python3
class Solution:
    # Version 1: Count
    # TC: O(logn) = O(1), SC: O(1)
    def FindLevel(self,N):
        node = 1
        h = 1
        count = 0
        while count < N:
            count += node
            node = node * (h + 1)
            h += 1
        return h - 1