#User function Template for python3
class Solution:
    # Version 1: Greedy
    # Start from the smallest number and subtract K for this.
    # For the following numbers, try to subtract first, then keep the same, then increase K.
    # Since we start from the smallest number and try to make the number small first, so we can get the maximum number of distinct numbers.
    # TC: O(n), SC: O(n)
    def distinctElements(self, N, K, A): 
        #code here
        A.sort()
        used = set()
        for val in A:
            if val - K not in used:
                used.add(val - K)
            elif val not in used:
                used.add(val)
            else:
                used.add(val + K)
        return len(used)