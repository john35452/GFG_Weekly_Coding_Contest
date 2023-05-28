class Solution:
    # Version 1: BFS
    # TC: O(n), SC: O(n)
    def density(self, N,  par):
        # code here
        graph = {k:[] for k in range(N)}
        root = -1
        for i in range(N):
            if par[i] < 0:
                root = i
            else:
                graph[par[i]].append(i)
        
        height = 0
        current = set([root])
        while current:
            nextStep = set()
            for node in current:
                for child in graph[node]:
                    nextStep.add(child)
            current = nextStep
            height += 1
        return N / height