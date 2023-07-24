from typing import List


class Solution:
    # Version 1: Greedy
    # Sort by exp_req and finish the most beneficial experiment
    # TC: O(nlogn), SC: O(n)
    def MaxXP(self, n : int, k : int, initial_exp : int, exp_req : List[int], exp_gain : List[int]) -> int:
        # code here
        import heapq
        req = [[exp_req[i], exp_gain[i]] for i in range(n)]
        req.sort()
        i = 0
        option = []
        power = initial_exp
        for _ in range(k):
            while i < n and req[i][0] <= power:
                heapq.heappush(option, [-req[i][1], req[i][0]])
                i += 1
            while option and option[0][1] > power:
                heapq.heappop(option)
            
            if option:
                inc, _ = heapq.heappop(option)
                power -= inc
            else:
                break
        return power
