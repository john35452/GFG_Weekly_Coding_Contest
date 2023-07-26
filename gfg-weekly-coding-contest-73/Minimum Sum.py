#User function Template for python3
class UnionFind:
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.size = [1]*n
    
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
            self.size[px] += self.size[py]
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
            self.rank[py] += 1
        return True
        
    def getSize(self, x):
        return self.size[self.find(x)]
        
class Solution:
    # Version 1: DFS(TLE)
    # Return the frequency of different minimum weight path
    # TC: O(n^2), SC: O(n^2)
    '''
    def minimumSum(self, n,weight, edges):
        #Code here
        
        import sys
        sys.setrecursionlimit(10**6)
        
        def dfs(node, parent, ans):
            res = {}
            res_child = []
            for child in graph[node]:
                if child != parent:
                    res_c = dfs(child, node, ans)
                    res_child.append(res_c)
                    for k, v in res_c.items():
                        new_weight = min(k, weight[node])
                        ans[0] += v * new_weight
                        if new_weight not in res:
                            res[new_weight] = 0
                        res[new_weight] += v
          
            
            for i in range(len(res_child)):
                for j in range(i + 1, len(res_child)):
                    left = res_child[i]
                    right = res_child[j]
                    for kl, vl in left.items():
                        for kr, vr in right.items():
                            new_weight = min(kl, kr, weight[node])
                            ans[0] += new_weight * vl * vr
                            
            if weight[node] not in res:
                res[weight[node]] = 0
            res[weight[node]] += 1
            return res
                        
        
        graph = {k:[] for k in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
         
        ans = [0]
        dfs(0, -1, ans)
        return ans[0]
    ''' 
    
    # Version 2: Improved version 1(TLE)
    # TC: O(n^2), SC: O(n^2)
    '''
    def minimumSum(self, n,weight, edges):
        #Code here
        
        import sys
        sys.setrecursionlimit(10**6)
        
        def dfs(node, parent, ans):
            res = {}
            res_child = []
            total = {}
            for child in graph[node]:
                if child != parent:
                    res_c = dfs(child, node, ans)
                    res_child.append(res_c)
                    for k, v in res_c.items():
                        new_weight = min(k, weight[node])
                        ans[0] += v * new_weight
                        if new_weight not in res:
                            res[new_weight] = 0
                        res[new_weight] += v
                        if k not in total:
                            total[k] = 0
                        total[k] += v
            
            
            #print(node, total, len(res_child), res_child)
            if len(res_child) > 1:
                extra = 0
                for res_c in res_child:
                    for kc, vc in res_c.items():
                        for ka, va in total.items():
                            new_weight = min(kc, ka, weight[node])
                            rest = va - res_c.get(ka, 0)
                            #print(kc, vc, ka, va, new_weight * vc * rest)
                            extra += new_weight * vc * rest
                ans[0] += extra // 2
                
            if weight[node] not in res:
                res[weight[node]] = 0
            res[weight[node]] += 1
            return res
                        
        
        graph = {k:[] for k in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
         
        ans = [0, 0]
        dfs(0, -1, ans)
        return ans[0]
    '''
    
    # Version 3: Improved version 2(TLE)
    # TC: O(n^2), SC: O(n^2)
    '''
    def minimumSum(self, n,weight, edges):
        #Code here
        
        import sys
        sys.setrecursionlimit(10**6)
        
        def dfs(node, parent, ans):
            res = {}
            res_child = []
            total = {}
            for child in graph[node]:
                if child != parent:
                    res_c = dfs(child, node, ans)
                    tmp = {}
                    for k, v in res_c.items():
                        new_weight = min(k, weight[node])
                        ans[0] += v * new_weight
                        if new_weight not in res:
                            res[new_weight] = 0
                        res[new_weight] += v
                        if new_weight not in tmp:
                            tmp[new_weight] = 0
                        tmp[new_weight] += v
                    res_child.append(tmp)
            
            
            #print(node, total, len(res_child), res_child)
            if len(res_child) > 1:
                extra = 0
                for res_c in res_child:
                    for kc, vc in res_c.items():
                        for ka, va in res.items():
                            new_weight = min(kc, ka)
                            rest = va - res_c.get(ka, 0)
                            #print(kc, vc, ka, va, new_weight * vc * rest)
                            extra += new_weight * vc * rest
                ans[0] += extra // 2
                
            if weight[node] not in res:
                res[weight[node]] = 0
            res[weight[node]] += 1
            return res
                        
        
        graph = {k:[] for k in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
         
        ans = [0]
        dfs(0, -1, ans)
        return ans[0]
    ''' 
    
    # Version 4: Improved version 3(TLE)
    # TC: O(n^2), SC: O(n^2)
    '''
    def minimumSum(self, n,weight, edges):
        #Code here
        
        import sys
        sys.setrecursionlimit(10**6)
        
        def dfs(node, parent, ans):
            res = {}
            for child in graph[node]:
                if child != parent:
                    res_c = dfs(child, node, ans)
                    for k, v in res_c.items():
                        new_weight = min(k, weight[node])
                        ans[0] += v * new_weight
                        for ka, va in res.items():
                            new_weight = min(k, weight[node], ka)
                            ans[0] += new_weight * v * va
                            
                    for k, v in res_c.items():
                        new_weight = min(k, weight[node])
                        if new_weight not in res:
                            res[new_weight] = 0
                        res[new_weight] += v
                
            if weight[node] not in res:
                res[weight[node]] = 0
            res[weight[node]] += 1
            return res
                        
        
        graph = {k:[] for k in range(n)}
        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)
         
        ans = [0]
        dfs(0, -1, ans)
        return ans[0]    
    '''
    
    # Version 5: Greedy + UnionFind
    # TC: O(n), SC: O(n)
    def minimumSum(self, n,weight, edges):
        #Code here
        edge = []
        for i in range(n - 1):
            x, y = edges[i]
            minv = min(weight[x], weight[y])
            edge.append([minv, x, y])
        #print(edge)
        edge.sort(reverse=True)
        disjoint = UnionFind(n)
        ans = 0
        for minv, x, y in edge:
            left = disjoint.getSize(x)
            right = disjoint.getSize(y)
            if disjoint.union(x, y):
                ans += minv * left * right
        return ans
    