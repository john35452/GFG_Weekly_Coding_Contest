needCompute = True
data = []

class Solution:
    # Version 1: Bitmask DP(TLE)
    # This is due to the test gets the result multiple times which requires us to store the result.
    # TC: O(logn * 2^10 * 10), SC: O(logn * 2^10 * 2)
    '''
    def totalNumbers(self, N : int) -> int:
        # code here
        def count(index, used, tight, dp):
            if index == m:
                return 1
            if (index, used, tight) in dp:
                return dp[index, used, tight]
            res = 0
            upper = 9
            if tight > 0:
                upper = int(ns[index])
            if used == 0:
                res += count(index + 1, used, 0, dp)
                for i in range(1, upper):
                    res += count(index + 1, 1<<i, 0, dp)
                res += count(index + 1, 1<<upper, tight, dp)
            elif used & (used - 1) == 0:
                for i in range(upper):
                    res += count(index + 1, used | 1<<i, 0, dp)
                res += count(index + 1, used | 1<<upper, tight, dp)
            else:
                for i in range(upper):
                    if used & (1<<i) > 0:
                        res += count(index + 1, used, 0, dp)
                res += count(index + 1, used, tight, dp)
            dp[index, used, tight] = res
            return dp[index, used, tight]
                
        ns = str(N)
        m = len(ns)
        dp = {}
        ans = count(0, 0, 1, dp)
        return ans
    '''
    
    # Version 2: Store all results
    # TC: O(10 * 10 * 2^11), SC: O(2^11)
    def totalNumbers(self, N : int) -> int:
        # code here
        from bisect import bisect_left
        global needCompute
        global data
        if needCompute:
            val = set()
            for mask in range(1<<11):
                for x in range(10):
                    for y in range(10):
                        num = 0
                        cur_mask = mask
                        while cur_mask > 0:
                            if cur_mask & 1 > 0:
                                num = 10 * num + x
                            else:
                                num = 10 * num + y
                            cur_mask >>= 1
                        val.add(num)
            data.extend(sorted(val))
            needCompute = False
        
        return bisect_left(data, N + 1)
    