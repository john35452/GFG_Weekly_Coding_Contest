#User function Template for python3

class Solution:
    # Version 1: Cycle
    # s[i] = s[i + K] = s[i + 2K] = .. = s[i]
    # Count the length of cycle, and check whether the frequency of character can be divided by the length.
    # We can use gcd(n, K) to know the smallest step.
    # TC: O(n), SC: O(n)
    def kPeriodic(self, s, K): 
        #code here
        import math
        from collections import Counter
        n = len(s)
        fre = Counter(s)
        group_count = math.gcd(n, K)
        item_count = n // group_count
        for _, v in fre.items():
            if v % item_count > 0:
                return "-1"
        keys = sorted(fre.keys())
        ans = [""]*n
        i = 0
        for c in sorted(fre.keys()):
            while fre[c] > 0:
                for s in range(item_count):
                    ans[i + s * group_count] = c
                fre[c] -= item_count
                i += 1
        return ''.join(ans)