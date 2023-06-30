
from typing import List


class Solution:
    # Version 1: Choose the minimum two dishes with different disliker
    # TC: O(nlogn), SC: O(n)
    '''
    def MinCost(self, n : int, prices : List[int], dislike : List[int]) -> int:
        # code here
        import heapq
        option = [[prices[i], dislike[i]] for i in range(n)]
        heapq.heapify(option)
        waiting = set()
        ans = 0
        while option:
            p, dis = heapq.heappop(option)
            if len(waiting) == 0:
                ans += p
                waiting.add(dis)
            elif dis not in waiting:
                ans += p
                return ans
        return -1
    '''
    
    # Version 2: Store the cheapest dish dislike by disliker
    # TC: O(n), SC: O(n)
    def MinCost(self, n : int, prices : List[int], dislike : List[int]) -> int:
        # code here
        dis = {}
        for i in range(n):
            if dislike[i] not in dis:
                dis[dislike[i]] = float('inf')
            dis[dislike[i]] = min(dis[dislike[i]], prices[i])
        
        if len(dis) < 2:
            return -1
        first = second = float('inf')
        for _, v in dis.items():
            if v < first:
                second = first
                first = v
            elif v < second:
                second = v
        return first + second