#User function Template for python3

class Solution:
    
    # Version 1: Greedy
    # If there are more than one employees in the same name group within the group, 
    # they won't focus on work.
    # Therefore, we only can make one employee in every name group to focus on work.
    # TC: O(n), SC: O(26) = O(1)
    def splitEmployees(self, s, n):
        fre = {}
        for employ in s:
            if employ[0] not in fre:
                fre[employ[0]] = 0
            fre[employ[0]] += 1
        ans = 0
        for _, v in fre.items():
            v -= 1
            if v > 1:
                ans += v
        return ans
