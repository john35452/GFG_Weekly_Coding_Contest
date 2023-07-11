#User function Template for python3
class Solution:
    # Version 1: Count
    # TC: O(n), SC: O(1)
    def separateStones(self,N,K,arr):
        #code here
        one = arr.count(1)
        zero = arr.count(0)
        ans = one // K + int(one % K > 0) + zero // K + int(zero % K > 0)
        return ans