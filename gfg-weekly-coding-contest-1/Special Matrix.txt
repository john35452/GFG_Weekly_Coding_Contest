#User function Template for python3

class Solution:
    # Version 1: Find the cost for each position
    # (x - a) * (x + (a + 1)) = x^2 + x - a(a + 1) = x^2 + x - 2P
    # P needs to be non-negative
    # a(a + 1) >= 0 => a >= 0 or a <= -1, and a need to be an integer.
    # With all these conditions a can be any interger
    # P = a(a+1) / 2
    # TC: O(n^2), SC: O(1)
    '''
    def minMoves (self, N, matrix):
        #code here
        for i in range(N):
            for j in range(N):
                val = matrix[i][j]
                k = int((2 * val) ** 0.5)
                matrix[i][j] = min(abs(val - (k * (k + 1)) // 2), abs(val - ((k + 1)*(k + 2))// 2))
        
        ans = float('inf')
        for i in range(N):
            res1 = res2 = 0
            for j in range(N):
                res1 += matrix[i][j]
                res2 += matrix[j][i]
            ans = min(ans, res1, res2)
        return ans
    '''
    
    # Version 2: Store all special numbers and binary search
    # TC: O(n^2 * log(50)), SC: O(50) = O(1)
    def minMoves (self, N, matrix):
        #code here
        from bisect import bisect_left
        special = []
        for i in range(50):
            special.append(i * (i + 1) // 2)
        for i in range(N):
            for j in range(N):
                index = bisect_left(special, matrix[i][j])
                res = special[index] - matrix[i][j]
                if index > 0:
                    res = min(res, matrix[i][j] - special[index - 1])
                matrix[i][j] = res
        
        ans = float('inf')
        for i in range(N):
            res1 = res2 = 0
            for j in range(N):
                res1 += matrix[i][j]
                res2 += matrix[j][i]
            ans = min(ans, res1, res2)
        return ans