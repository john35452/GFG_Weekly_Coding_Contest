#User function Template for python3

class Solution:
    # Version 1: Binary Search
    # We can use min heap to know when will a seat can be released.
    # It takes O(nlogn) for each check.
    # TC: O(nlogn * logn), SC: O(n)
    def minimizeComputers(self, n, k, arr):
        # code here
        import heapq
        
        def check(seat):
            res = 0
            option = arr[:seat]
            heapq.heapify(option)
            i = seat
            while option or i < n:
                t = heapq.heappop(option)
                res = max(res, t)
                if i < n:
                    heapq.heappush(option, t + arr[i])
                    i += 1
            return res
        
        
        l = 1
        r = n
        while l < r:
            m = l + (r - l) // 2
            if check(m) <= k:
                r = m
            else:
                l = m + 1
        return l
                