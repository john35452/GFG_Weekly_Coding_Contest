class Solution:
    # Version 1: Top down DP
    # dp[i][bal][j][pre]: The number of distinct valid string we can find 
    # starting from index i, balance bal, j consecutive bucket and pre as the last character.
    # TC: O(n^2 * k), SC: O(n^2 * k)
    def countStrings(self, n : int, s : str, k : int) -> int:
        # code here
        
        def count(index, balance, cont, pre, dp):
            if balance < 0 or cont > k:
                return 0
            elif index == n:
                return int(balance == 0)
            elif s[index] == '(':
                nextCnt = cont + 1 if pre == '(' else 1
                return count(index + 1, balance + 1, nextCnt, '(', dp)
            elif s[index] == ')':
                nextCnt = cont + 1 if pre == ')' else 1
                return count(index + 1, balance - 1, nextCnt, ')', dp)
            elif (index, balance, cont, pre) in dp:
                return dp[index, balance, cont, pre]
            else:
                res = 0
                if pre == '(':
                    res = (res + count(index + 1, balance + 1, cont + 1, '(', dp)) % M
                    res = (res + count(index + 1, balance - 1, 1, ')', dp)) % M
                else:
                    res = (res + count(index + 1, balance + 1, 1, '(', dp)) % M
                    res = (res + count(index + 1, balance - 1, cont + 1, ')', dp)) % M
                
                dp[index, balance, cont, pre] = res
                return dp[index, balance, cont, pre]
        
        dp = {}
        M = 10**9 + 7
        ans = count(0, 0, 0, '(', dp)
        return ans
    