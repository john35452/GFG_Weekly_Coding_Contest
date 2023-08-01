#User function Template for python3

class Solution:
    # Version 1: Cases
    # 1. s in t
    # 2. t in s
    # 3. Put t behind s
    # 4. Put s behind t
    # Check the first two cases first, if not get the smaller one from option 3 and 4.
    # TC: O(mn), SC: O(m + n)
    def commonString(self, s, t):
        #code here
        if s in t:
            return t
        if t in s:
            return s
        m = len(s)
        n = len(t)
        ans = min(s + t, t + s)
        
        for l in range(min(m, n), 0, -1):
            if s[-l:] == t[:l]:
                ns = s + t[l:]
                if len(ns) < len(ans) or (len(ns) == len(ans) and ns < ans):
                    ans = ns
                break
        
        for l in range(min(m, n), 0, -1):
            if t[-l:] == s[:l]:
                ns = t + s[l:]
                if len(ns) < len(ans) or (len(ns) == len(ans) and ns < ans):
                    ans = ns
                break
        return ans
        
               