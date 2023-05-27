#User function Template for python3

class Solution:
    # Version 1: Inplace
    # TC: O(n), SC: O(1)
    def binaryArray(self, n, arr):
        #code here
        total = sum(arr)
        for i in range(n):
            arr[i] = int((total - arr[i]) % 2 == 0) 
        return arr