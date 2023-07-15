#User function Template for python3

class Solution:
    # Version 1: Greedy(TLE)
    # Start with whole s, if we can divide it into two same string, then divide it.
    # TC: O(n^2), SC: O(n)
    '''
    def secretCipher(self,s):
        #code here
        def check(i):
            half = (i + 1) // 2
            for k in range(half):
                if s[k] != s[half + k]:
                    return False
            return True
        
        n = len(s)
        ans = []
        j = n - 1
        while j >= 0:
            #print(j)
            if j % 2 > 0 and check(j):
                ans.append("*")
                j //= 2
            else:
                ans.append(s[j])
                j -= 1
        
        return ''.join(reversed(ans))
    '''
        
    # Version 2: KMP
    # If the prefix and suffix of s[:i + 1] are the same, we can use "*", otherwise use s[i].
    # TC: O(n), SC: O(n)
    def secretCipher(self,s):
        #code here
        def check(j):
            leng = pi[j] + 1
            if 2 * leng < j + 1:
                return False
            half = (j + 1) // 2
            for i in range(half):
                if s[i] != s[half + i]:
                    return False
            return True
            
        n = len(s)
        pi = [0, 0]
        j = 0
        for i in range(1, n):
            while j > 0 and s[i] != s[j]:
                j = pi[j]
            if s[i] == s[j]:
                j += 1
            pi.append(j)
        #print(pi)
        
        ans = []
        j = n - 1
        while j >= 0:
            if j % 2 > 0 and check(j):
                ans.append("*")
                j //= 2
            else:
                ans.append(s[j])
                j -= 1
        
        return ''.join(reversed(ans))