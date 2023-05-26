#User function Template for python3

class Solution:
    # Version 1: Top down DP (TLE)
    # It takes much more space and takes time.
    # TC: O(kE), SC: O(kV)
    '''
    def expectedApples(self, V, E, arr, edges, k):
        # code here
        def start(node, step, dp):
            if step == 0:
                return 0
            elif (node, step) not in dp:
                res = 0
                for v in graph[node]:
                    res = (res + start(v, step - 1, dp)) % M
                res = (arr[node] + (res * pow(len(graph[node]), M - 2, M)) % M) % M
                dp[node, step] = res
            return dp[node, step]
            
        M = 10**9 + 7
        graph = {i:[] for i in range(V)}
        for x, y in edges:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        
        dp = {}
        ans = 0
        for i in range(V):
            ans = (ans + start(i, k, dp)) % M
        return (ans * pow(V, M - 2, M)) % M
    '''
    
    # Version 2: Bottom up DP
    # dp[i]: the expected number to get apples from i node for K seconds
    # Since M is a prime number, a^-1 % M = a^(M - 2) % M
    # TC; O(kE), SC: O(V+E)
    def expectedApples(self, V, E, arr, edges, k):
        # code here
        M = 10**9 + 7
        graph = {i:[] for i in range(V)}
        for x, y in edges:
            graph[x - 1].append(y - 1)
            graph[y - 1].append(x - 1)
        
        dp = [0]*V

        ans = 0
        for i in range(k):
            nextDp = [0]*V
            for j in range(V):
                for v in graph[j]:
                    nextDp[j] = (nextDp[j] + dp[v]) % M
                nextDp[j] = (arr[j] + nextDp[j] * pow(len(graph[j]), M - 2, M)) % M
            dp = nextDp
            #print(i, ans)
        return (sum(dp) * pow(V, M - 2, M)) % M
        