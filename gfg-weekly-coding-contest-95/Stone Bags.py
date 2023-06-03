#User function Template for python3

class Solution:
    # Version 1: Greedy
    # The problem description is unclear.
    # We only can decide how we are going to distribute stones, but we cannot decide which stones will be picked.
    # The goal is find the maximum value for the minimum score among all kinds of distribution.
    # We can sort arr and consider two case.
    # Case 1:
    #   Group 1: [arr[0], .. arr[i]] 
    #   Group 2: [arr[i + 1], ..., arr[n - 2]] 
    #   Group 3: [arr[n]]
    #   score: arr[n - 1] - arr[i] + arr[i + 1] - arr[i]
    
    # Case 2:
    #   Group 1: [arr[0]]
    #   Group 2: [arr[1], ... , arr[i - 1]]
    #   Group 3: [arr[i], ..., arr[n - 1]]
    #   Score: arr[i] - arr[0] + arr[i] - arr[i - 1]
    # TC: O(nlogn), SC: O(1)
    def stoneBags(self, n, arr):
        # code here
        arr.sort()        
        ans = 0
        for i in range(n - 2):
            ans = max(ans, arr[n - 1] - arr[i] + arr[i + 1] - arr[i])
        
        for i in range(n - 1, 0, -1):
            ans = max(ans, arr[i] - arr[0] + arr[i] - arr[i - 1])
        return ans
        
        