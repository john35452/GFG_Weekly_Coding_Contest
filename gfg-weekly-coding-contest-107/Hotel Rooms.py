
from typing import List


class Solution:
    # Version 1: DP (TLE)
    # dp[bitmask, remaining_k]: The minimum rooms needed starting with bitmask used state and remaining_k.
    # TC: O(2^n * n * n), SC: O(2^n * k)
    '''
    def roomsRequired(self, N : int, K : int, students : List[int]) -> int:
        # code here
        def pick(used, remaining, dp):
            if used == (1<<N) - 1:
                return 1
            if (used, remaining) in dp:
                return dp[used, remaining]
            res = float('inf')
            done = True
            for i in range(N):
                if used & (1 << i) == 0:
                    if (students[i] <= remaining):
                        done = False
                        res = min(res, pick(used | (1<<i), remaining - students[i], dp))
                    else:
                        break
            if done:
                res = min(res, pick(used, K, dp) + 1)
            dp[used, remaining] = res
            return dp[used, remaining]
        
        students.sort()
        dp = {}
        return pick(0, K, dp)
    '''
    
    # Version 2: Greedy (WA)
    # Sort all students and start with the biggest one.
    # This solution works due to the weak test case, and it doesn't work now.
    # TC: O(nlogn), SC: O(n)
    '''
    def roomsRequired(self, N : int, K : int, students : List[int]) -> int:
        import math
        
        def fill(index, space, ans):
            if index == N:
                res = 0
                for i in range(N - 1, -1, -1):
                    if space[i] != K:
                        res = i
                        break
                if not ans:
                    ans.append(res + 1)
            elif not ans:
                    
                for i in range(N):
                    if space[i] >= students[index]:
                        space[i] -= students[index]
                        fill(index + 1, space, ans)
                        space[i] += students[index]
                
        students.sort(reverse=True)
        space = [K]*N
        ans = []
        fill(0, space, ans)
        return ans[0]
    '''
    
    # Version 3: Bitmask DP
    # dp[mask] : The minimum number of positions needs to put students with bitmask mask
    # TC: O(n * 2^n), SC: O(2^n)
    def roomsRequired(self, N : int, K : int, students : List[int]) -> int:
        # code here
        dp = [float('inf')]*(1<<N)
        dp[0] = 0
        for mask in range(1<<N):
            for i in range(N):
                if mask & (1 << i) == 0:
                    room = dp[mask] // K
                    count = dp[mask] % K
                    if count + students[i] <= K:
                        count += students[i]
                    else:
                        room += 1
                        count = students[i]
                    dp[mask | (1<<i)] = min(dp[mask | (1<<i)], K * room + count)
        
        return dp[-1] // K + int(dp[-1] % K > 0)
    