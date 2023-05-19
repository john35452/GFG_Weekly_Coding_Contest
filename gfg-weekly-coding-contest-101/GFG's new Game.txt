#User function Template for python3

class Solution:
    # Version 1: Greedy
    # Join the most beneficial contest as many as possible
    # TC: O(nlogn), SC: O(n)
    def gfgGame(self, N, G, require, receive):
        #code here
        import heapq
        option = []
        for i in range(N):
            option.append([require[i] - receive[i], -require[i]])
        heapq.heapify(option)
        ans = 0
        while option and G > 0:
            cost, demand = heapq.heappop(option)
            demand = -demand
            #print(G, cost, demand, i)
            if G >= demand:
                diff = G - demand
                time = diff // cost + 1
                G -= cost * time
                ans += time
        return ans