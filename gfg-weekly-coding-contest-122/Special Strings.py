#User function Template for python3

class Solution:
    # Version 1: Digit DP
    # TC: O(n * 26 * 26 * 2 * 26), SC: O(n * 26 * 26) 
    '''
    def specialStrings(self, N, S):

        def count(index, pre, last, greater, dp):
            if index == N:
                return int(greater)
            if (index, pre, last, greater) in dp:
                return dp[index, pre, last, greater]
            res = 0
            lower = 0
            if not greater:
                lower = ord(S[index]) - ord('a')
            if lower != pre and lower != last:
                res = (res + count(index + 1, last, lower, greater, dp)) % M
            for i in range(lower + 1, 26):
                if i != last and i != pre:
                    res = (res + count(index + 1, last, i, True, dp)) % M
            dp[index, pre, last, greater]  = res
            return res
            
        M = 10**9 + 7
        dp = {}
        ans = count(0, -1, -1, False, dp)
        return ans
    '''
    
    # Version 2: Count('zzz') - Count(s)
    # TC: O(n * 26 * 26 * 2 * 26), SC: O(n * 26 * 26)
    def specialStrings(self, N, S):

        def count(index, pre, last, strict, dp):
            if index == N:
                return 1
            if (index, pre, last, strict) in dp:
                return dp[index, pre, last, strict]
            res = 0
            upper = 25
            if strict:
                upper = ord(S[index]) - ord('a')
            if pre != upper and last != upper:
                res = (res + count(index + 1, last, upper, strict, dp)) % M
            for i in range(upper):
                if i != last and i != pre:
                    res = (res + count(index + 1, last, i, False, dp)) % M
            
            dp[index, pre, last, strict]  = res
            return res
            
        M = 10**9 + 7
        dp = {}
        z = count(0, -1, -1, False, dp)
        bound = count(0, -1, -1, True, dp)
        return (z - bound) % M 
