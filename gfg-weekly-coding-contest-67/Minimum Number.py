#User function Template for python3

class Solution:
    
    # Version 1: Mod
    # We can always use the smallest value to subtract the bigger one.
    # TC; O(n), SC: O(1)
    '''
    def minimumNumber(self, n, arr):
        minv = min(arr)
        for val in arr:
            new_val = val % minv
            if new_val > 0:
                minv = new_val
        return minv
    '''
    
    # Version 2: GCD
    # Consider two number a, b
    # If a > b, we will subtract b several times until b > a which means a = a % b
    # At this moment, their role can be reversed and do the same thing again.
    # This process is the same as getting gcd of a, b.
    # Therefore, the final result is the gcd of all numbers
    # TC: O(n * log(max(arr))), SC: O(1)
    def minimumNumber(self, n, arr):
        minv = min(arr)
        for val in arr:
            new_val = val % minv
            if new_val > 0:
                minv = new_val
        return minv
    
        