#User function Template for python3

class Solution:
    # Version 1: Greedy and cases
    # Connect all nodes to the root
    # Check three cases for root
    # Root val:
    # 1. 0
    # 2. minv
    # 3. Original value
    # TC: O(n), SC: O(1)
    def solve(self,n ,Par, Arr, K, A, B):
        # code here
        if A > B:
            A = B
        minv = min(Arr)
        ans = float('inf')
        sum1 = B
        for i in range(1, n):
            if Arr[i] > K:
                sum1 += A
        ans = min(ans, sum1)
        
        if minv <= K:
            sum2 = A
            val = minv
            new_minv = minv
            for i in range(1, n):
                if val + Arr[i] > K:
                    if val + new_minv > K:
                        new_minv = 0
                        sum2 += B
                    else:
                        sum2 += A
            ans = min(ans, sum2)
            
        if Arr[0] <= K:
            sum3 = 0
            val = Arr[0]
            new_minv = minv
            for i in range(1, n):
                if val + Arr[i] > K:
                    if val + new_minv > K:
                        new_minv = 0
                        sum3 += B
                    else:
                        sum3 += A
            ans = min(ans, sum3)
        return ans