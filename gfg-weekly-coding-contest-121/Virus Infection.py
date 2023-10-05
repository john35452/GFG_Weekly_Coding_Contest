#User function Template for python3
class Solution:
    # Version 1: Diff array
    # TC: O(n), SC: O(n)
    def solve(self, s, K): 
        #code here
        n = len(S)
        diff = [0]*(n + 1)
        for i in range(n):
            if s[i] == '1':
                diff[max(i - K, 0)] += 1
                diff[min(i + K + 1, n)] -= 1
        
        ans = 0
        cur = 0
        for i in range(n):
            cur += diff[i]
            if cur > 0:
                ans += 1
        return ans
        

