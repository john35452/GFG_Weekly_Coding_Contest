#User function Template for python3

class Solution:
    # Version 1: Get the formula and try to find the maximum value
    # score = val + 2 * val + 4 * val + ... = val * (1 + 2 + 4 + ...) = val * (2^(i + 1) - 1) 
    # TC: O(logk), SC: O(1)
    def acceptTheChallenge(self, k):
        # code here
        import math
        time = int(math.log(k, 2))
        for i in range(1, time):
            val = (2**(i + 1)) - 1
            if val <= k and k % val == 0:
                return k // val
        return -1
        