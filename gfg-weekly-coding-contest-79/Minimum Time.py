from typing import List


class Solution:
    # Version 1: DP
    # dp[i]: The minimum of time to solve (i - 1) th questions
    # TC: O(nk), SC: O(n)
    '''
    def minTime(self, n : int, time : List[int], search : List[int], k : int) -> int:
        # code here
        
        dp = [float('inf')]*(n + 1)
        dp[0] = 0
        for i in range(n):
            dp[i + 1] = time[i] + dp[i]
            for j in range(k):
                if i - j < 0:
                    break
                dp[i + 1] = min(dp[i + 1], dp[i - j] + search[i - j])
        return dp[-1]
    '''
    
    # Version 2: Improved version 1
    # Use heap to get the minimum value from last k results
    # TC: O(nlogk), SC: O(n)
    '''
    def minTime(self, n : int, time : List[int], search : List[int], k : int) -> int:
        # code here
        import heapq        
        dp = [float('inf')]*(n + 1)
        dp[0] = 0
        option = []
        for i in range(n):
            dp[i + 1] = time[i] + dp[i]
            while option and option[0][1] < i - k + 1:
                heapq.heappop(option)
            heapq.heappush(option, [dp[i] + search[i], i])
            dp[i + 1] = min(dp[i + 1], option[0][0])
        return dp[-1]
    '''
    
    # Version 3: Improved version 2
    # Use monotonic queue to get the minimum value in last k results
    # TC: O(n), SC: O(n)
    '''
    def minTime(self, n : int, time : List[int], search : List[int], k : int) -> int:
        # code here
        from collections import deque
        dp = [float('inf')]*(n + 1)
        dp[0] = 0
        option = deque()
        for i in range(n):
            dp[i + 1] = time[i] + dp[i]
            while option and option[0][1] < i - k + 1:
                option.popleft()
            val = dp[i] + search[i]
            while option and option[-1][0] >= val:
                option.pop()
            option.append([val, i])
            dp[i + 1] = min(dp[i + 1], option[0][0])
        return dp[-1]
    '''
    
    # Version 4: Improved version 3
    # TC: O(n), SC: O(k)
    '''
    def minTime(self, n : int, time : List[int], search : List[int], k : int) -> int:
        # code here
        from collections import deque
        dp = 0
        nextDp = float('inf')
        option = deque()
        for i in range(n):
            nextDp = time[i] + dp
            while option and option[0][1] < i - k + 1:
                option.popleft()
            val = dp + search[i]
            while option and option[-1][0] >= val:
                option.pop()
            option.append([val, i])
            nextDp = min(nextDp, option[0][0])
            dp, nextDp = nextDp, dp
        return dp
    '''
    
    # Version 5: Consider in the reverse direction
    # TC: O(n), SC: O(n)
    def minTime(self, n : int, time : List[int], search : List[int], k : int) -> int:
        # code here
        from collections import deque
        dp = [float('inf')]*(n + 1)
        dp[n] = 0
        option = deque()
        option.append(n)
        for i in range(n - 1, -1, -1):
            dp[i] = time[i] + dp[i + 1]
            while option and option[0] > i + k:
                option.popleft()
            dp[i] = min(dp[i], dp[option[0]] + search[i])
            while option and dp[option[-1]] >= dp[i]:
                option.pop()
            option.append(i)
        return dp[0]