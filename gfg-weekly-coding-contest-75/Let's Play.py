#User function Template for python3

from typing import List

class Solution:
    # Version 1: DP
    # dp[index, diff, pre]: Return the list of valid scores starts with the state
    # TC: O(n * 10 * 10 * 10), SC: O(n * 10 * 10 * 10)
    '''
    def letsPlay(self, N : int, A: List[int], arr : List[int]) -> None:
        import sys
        sys.setrecursionlimit(10**6)
        
        def play(index, diff, pre, dp):
            if index == N:
                return ["Y"]
            if (index, diff, pre) in dp:
                return dp[index, diff, pre]
            res = []
            for i in range(max(1, diff + 1), 11):
                if i != pre and A[i - 1] > 0:
                    res = play(index + 1, i - diff, i, dp)
                    if len(res) > 0:
                        res.append(i)
                        break
            dp[index, diff, pre] = res
            return dp[index, diff, pre]
        
        dp = {}
        ans = play(0, 0, 0, dp)
        if ans:
            for i in range(N):
                arr.append(ans[N - i]);
        #print(ans)
        return len(ans) > 0
    '''
    
    # Version 2: Recursive with strict contraints
    # TC: O(10 ^ n), SC: O(n)
    '''
    def letsPlay(self, N : int, A: List[int], arr : List[int]) -> None:
        import sys
        sys.setrecursionlimit(10**6)
        
        def play(index, diff, pre, arr):
            if index == N:
                return True
            res = False
            for i in range(max(1, diff + 1), 11):
                if i != pre and A[i - 1] > 0:
                    arr.append(i)
                    if play(index + 1, i - diff, i, arr):
                        res = True
                        break
                    arr.pop()
            return res
            
        return play(0, 0, 0, arr) 
    '''  

    # Version 3: Improved version 1
    # Use dp to store the result with specific state
    # We can have early stop due to this dp
    # It's not possible to meet a visited state with true result,
    # because we would already get the true result from that.
    # TC: O(n * 10 * 10 * 10), SC: O(n * 10 * 10)
    def letsPlay(self, N : int, A: List[int], arr : List[int]) -> None:
        import sys
        sys.setrecursionlimit(10**6)
        
        def play(index, diff, pre, dp, arr):
            if index == N:
                return True
            if (index, diff, pre) in dp:
                return dp[index, diff, pre]
            res = False
            for i in range(max(1, diff + 1), 11):
                if i != pre and A[i - 1] > 0:
                    arr.append(i)
                    if play(index + 1, i - diff, i, dp, arr):
                        res = True
                        break
                    arr.pop()
            dp[index, diff, pre] = res
            return dp[index, diff, pre]
        
        dp = {}
        return play(0, 0, 0, dp, arr)