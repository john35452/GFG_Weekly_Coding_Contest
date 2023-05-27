#User function Template for python3
class Solution:
    # Version 1: Dijkstra
    # TC: O(VlogE), SC: O(E + V)
    def minTime(self, N, X, src, dest, M1, M2, airlines, railways):
        #code here
        import heapq
        dis_a = {}
        dis_t = {}
        graph_a = {k:{} for k in range(N)}
        graph_t = {k:{} for k in range(N)}
        for x, y, c in airlines:
            graph_a[x][y] = c
        for x, y, c in railways:
            graph_t[x][y] = c
        option = [(0, src, True), (0, src, False)]
        heapq.heapify(option)
        while option:
            d, node, isAir = heapq.heappop(option)
            if (isAir and node not in dis_a) or (not isAir and node not in dis_t):
                if isAir:
                    dis_a[node] = d
                else:
                    dis_t[node] = d
                for neighbor, c in graph_a[node].items():
                    if neighbor not in dis_a:
                        if (isAir is None) or isAir:
                            newCost = d + c
                        else:
                            newCost = d + c + X
                        heapq.heappush(option, (newCost, neighbor, True))
                for neighbor, c in graph_t[node].items():
                    if neighbor not in dis_t:
                        if (isAir is None) or (not isAir):
                            newCost = d + c
                        else:
                            newCost = d + c + X
                        heapq.heappush(option, (newCost, neighbor, False))
        if dest in dis_a or dest in dis_t:
            return min(dis_a.get(dest, float('inf')), dis_t.get(dest, float('inf')))
        else:
            return -1