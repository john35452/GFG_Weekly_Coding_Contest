from typing import List


class Solution:
    # Similar question as the below question in Leetcode
    # https://leetcode.com/problems/two-best-non-overlapping-events/
    
    # Version 1: Heap 
    # Get the maximum coin we can get by all ranges before current time
    # TC: O(nlogn), SC: O(n)
    '''
    def maxCoins(self, n : int, ranges : List[List[int]]) -> int:
        # code here
        import heapq
        ranges.sort()
        option = []
        maxv = 0
        ans = 0
        for s, e, v in ranges:
            while option and option[0][0] <= s:
                item = heapq.heappop(option)
                maxv = max(maxv, item[1])
            ans = max(ans, v + maxv)
            heapq.heappush(option, [e, v])
        return ans
    '''
    
    # Version 2: DP
    # Use binary search to find the location before the range
    # We only can search within the ranges before the current range
    # otherwise it will cause wrong answer
    # TC: O(nlogn), SC: O(n)
    def maxCoins(self, n : int, ranges : List[List[int]]) -> int:
        # code here
        from bisect import bisect_left
        ranges.sort(key = lambda x:(x[1], x[0]))
        dp = [0]*(n + 1)
        pre = []
        ans = 0
        for i in range(n):
            #print(i, ranges[i], dp)
            index = bisect_left(pre, ranges[i][0] + 1)
            ans = max(ans, dp[index] + ranges[i][2])
            dp[i + 1] = max(dp[i], ranges[i][2])
            pre.append(ranges[i][1])
        return ans
    
