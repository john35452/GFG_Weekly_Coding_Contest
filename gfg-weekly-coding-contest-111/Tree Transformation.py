from typing import List


class Solution:
    # Version 1: Greedy
    # Count the number of non-leaf nodes
    # They should be merged into one node
    # TC: O(n), SC: O(n)
    def solve(self, N : int, p : List[int]) -> int:
        # code here
        edges = [0]*N
        for i in range(1, N):
            edges[p[i]] += 1
            edges[i] += 1
        count = 0
        for i in range(N):
            if edges[i] > 1:
                count += 1
        return max(count - 1, 0)
