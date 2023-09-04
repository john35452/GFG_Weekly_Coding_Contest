#User function Template for python3
class Solution:
    # Version 1: DP + prefix sum
    # Count the number of odd numbers before one number
    # For each entry in the stack, the value is (index, prefix sum to the number of i, j pairs)
    # TC: O(n), SC: O(n)
    '''
    def countTriplet(self, N, A, X): 
        # code here
        from collections import deque
        before = [0]*(N + 1)
        for i in range(N):
            before[i + 1] = before[i] + int(A[i] % 2 > 0)
        #print(before)
        stack = deque([[-1, 0]])
        cur = 0
        ans = 0
        l = 0
        for i in range(N):
            if A[i] % 2 > 0:
                while l < len(stack) and i - stack[l][0] >= X:
                    l += 1
                if l > 0:
                    ans += stack[l - 1][1]
                if i - X >= 0:
                    stack.append([i, stack[-1][1] + before[i - X + 1]])    
                #print(i, A[i], stack, ans)
        return ans
    '''
    
    # Version 2: Consider the number of odd before and after X positions
    # TC: O(n), SC: O(n)
    '''
    def countTriplet(self, N, A, X): 
        # code here
        before = [0]*(N + 1)
        for i in range(N):
            before[i + 1] = before[i] + int(A[i] % 2 > 0)
        ans = 0
        for i in range(N):
            if A[i] % 2 > 0:
                if i >= X and i + X < N:
                    ans += before[i - X + 1] * (before[-1] - before[i + X])
        return ans
    '''
    
    # Version 3: Improved version 2
    # TC: O(n), SC: O(1)
    def countTriplet(self, N, A, X): 
        # code here
        first = second = 0
        for i in range(X, N):
            if A[i] % 2 > 0:
                second += 1
        ans = 0
        for i in range(N):
            if i - X >= 0 and A[i - X] % 2 > 0:
                first += 1
            if A[i] % 2 > 0:
                ans += first * second
            if i + X < N and A[i + X] % 2 > 0:
                second -= 1
        return ans

