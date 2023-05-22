#User function Template for python3

class Solution:
    # Version 1: Choose the closest position
    # TC: O(logn), SC: O(1) 
    def refueling(self, X):
        # code here
        ans = 1
        while ans < X:
            ans <<= 1
          
        if abs(X - (ans >> 1)) < abs(ans - X):
            return ans >> 1
        else:
            return ans