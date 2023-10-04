#User function Template for python3

class Solution:
    # Version 1: Greedy
    # The optimal change for one number is to make every bit 1, and this is same as ignoring this number.
    # Therefore, we can consider all answers without each number.
    # We can use prefix and suffix AND results to deal with this.
    # TC: O(n), SC: O(n)
    '''
    def maxAnd(self, N, A):
        #code here
        ans = 0
        left = [0]*(N + 1)
        right = [0]*(N + 1)
        left[0] = right[-1] = (1<<32) - 1
        for i in range(N):
            left[i + 1] = left[i] & A[i]
        
        for i in range(N - 1, -1, -1):
            right[i] = right[i + 1] & A[i]
        
        for i in range(N):
            ans = max(ans, left[i] & right[i + 1])
        
        return ans
    '''
    
    # Version 2: Simplify the prefix
    # TC: O(n), SC: O(n)
    def maxAnd(self, N, A):
        #code here
        ans = 0
        suffix = [0]*(N + 1)
        suffix[-1] = (1<<32) - 1
        
        for i in range(N - 1, -1, -1):
            suffix[i] = suffix[i + 1] & A[i]
        
        prefix = (1<<32) - 1
        for i in range(N):
            ans = max(ans, prefix & suffix[i + 1])
            prefix &= A[i]
        return ans
    