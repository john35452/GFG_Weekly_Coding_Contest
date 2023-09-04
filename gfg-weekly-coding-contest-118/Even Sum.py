#User function Template for python3

class Solution:
    # Version 1: Count the number of odd number
    # Also get the minimum cost to change an even number to an odd number
    # TC: O(nlogn), SC: O(1)
    def solve(self, A, N):
        odd = 0
        cost = float('inf')
        for val in A:
            if val % 2 > 0:
                odd += 1
            else:
                cur = 0
                while val > 0 and val % 2 == 0:
                    val >>= 1
                    cur += 1
                cost = min(cost, cur)
        if odd % 2 == 0:
            return 0
        elif cost != float('inf'):
            return cost
        else:
            return -1



