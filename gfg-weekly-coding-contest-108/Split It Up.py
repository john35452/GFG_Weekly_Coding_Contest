
from typing import List


class Solution:
    # Version 1: Cut from every edge in DFS
    # TC: O(n), SC: O(n)
    def MinDiff(self, n : int, A : List[int], B : List[int]) -> int:
        # code here
        def dfs(node, parent, ans):
            res = node
            for child in graph[node]:
                if child != parent:
                    res += dfs(child, node, ans)
            ans[0] = min(ans[0], abs(total - res - res))
            return res
            
        graph = {k:[] for k in range(1, n + 1)}
        for i in range(n - 1):
            graph[A[i]].append(B[i])
            graph[B[i]].append(A[i])
            
        ans = [float('inf')]
        total = n * (n + 1) // 2

        for child in graph[1]:
            dfs(child, 1, ans)
        return ans[0]
