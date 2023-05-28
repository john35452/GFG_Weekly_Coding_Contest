#User function Template for python3

class Solution:
    # Version 1: LCA and DP
    # If the LCA of x and y is x or y, they are in the same subtree.
    # We can store the subtree gcd in a list and use them later.
    # We can use DFS to find LCA and fill in the result list of gcd subtree.
    # TC: O(nlog(max(val)), SC: O(n)
    def gcdTree(self, n, edges, val, x, y):
        # code here
        import math
        def dfs(node, p, ans):
            res = val[node]
            count = int(node in (x, y))
            for v in graph[node]:
                if v != p:
                    child = dfs(v, node, ans)
                    res = math.gcd(res, child[0])
                    count += child[1]
            if count == 2:
                if len(ans) == 0:
                    ans.append(node)
            gcd[node] = res
            return res, count
                    
            
        graph = {k:[] for k in range(n)}
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        root = 0
        ans = []
        gcd = list(val)
        dfs(root, -1, ans)
        if ans[0] in (x, y):
            return -1
        else:
            return math.gcd(gcd[x], gcd[y])
        