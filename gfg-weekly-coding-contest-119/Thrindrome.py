#User function Template for python3

class Solution():
    # Version 1: Count the occurence of each alphbet in each subtree
    # TC: O(n), SC: O(n)
    def solve(self, N, p, C):
        #your code goes here
        from collections import Counter
        
        def dfs(node, ans):
            res = {C[node]: 1}
            for child in graph[node]:
                tmp = dfs(child, ans)
                for k, v in tmp.items():
                    res[k] = res.get(k, 0) + v
                    remain = total[k] - v - int(C[node] == k)
                    ans[0] += v * remain
                    
            for k, v in res.items():
                remain = total[k] - v
                ans[0] += (v - int(C[node] == k)) * remain
                
            return res
                
        total = Counter(C)
        graph = {k:[] for k in range(N)}
        for i in range(1, N):
            graph[p[i]].append(i)
            
        ans = [0]
        dfs(0, ans)
        
        return ans[0]
