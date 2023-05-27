#User function Template for python3
class UnionFind:
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
        else:
            self.parent[px] = py
            self.rank[py] += 1
        return True
    
class Solution:
    # Version 1: DFS
    # TC: O(V+E), SC: O(V)
    '''
    def destroyTheGarden(self, n, m, arr, overlapped):
        # code here
        import sys
        sys.setrecursionlimit(1000000)
        
        def dfs(node):
            res = arr[node]
            used[node] = True
            for overlap in graph[node]:
                if not used[overlap]:
                    res = max(res, dfs(overlap))
            return res
        
        graph = {k:[] for k in range(n)}
        for x, y in overlapped:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        
        ans = 0
        used = [False]*n
        for i in range(n):
            if not used[i]:
                ans += dfs(i)
        return ans
    '''
    
    # Version 2: Union Find
    # TC: O(V + E), SC: O(V)
    def destroyTheGarden(self, n, m, arr, overlapped):
        # code here
        
        disjoint = UnionFind(n)
        for x, y in overlapped:
            disjoint.union(x - 1, y - 1)
            
        ans = 0
        data = {}
        for i in range(n):
            p = disjoint.find(i)
            if p not in data:
                data[p] = 0
            data[p] = max(data[p], arr[i])
        return sum(data.values())
        