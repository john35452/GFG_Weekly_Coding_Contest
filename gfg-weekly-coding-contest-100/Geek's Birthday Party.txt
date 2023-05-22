#User function Template for python3

from typing import List
import sys
sys.setrecursionlimit(10**6)
class Solution:
    # Version 1: Greedy
    # Sort by depth - child_count
    # TC: O(nlogm), SC: O(m)
    def findMaxSnacks(self, n : int, m : int, edges : List[List[int]]) -> int:
        #code here
        import heapq
        
        def dfs(node, parent, cur_depth, child_count, depth):
            depth[node] = cur_depth
            res = 0
            for child in graph[node]:
                if child != parent:
                    res += dfs(child, node, cur_depth + 1, child_count, depth)
            child_count[node] = res
            return res + 1
            
        graph = {k:[] for k in range(1, n + 1)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
        
        child_count = [0]*(n + 1)
        depth = [0]*(n + 1)
        
        dfs(1, None, 0, child_count, depth)
        option = []
        for i in range(1, n + 1):
            heapq.heappush(option, depth[i] - child_count[i])
            if len(option) > m:
                heapq.heappop(option)
                
        return sum(option)
        