#User function Template for python3

class Solution:
    # Version 1: Math
    # Each digit can be 1, 3, 5, 7, 9
    # 1th: 1   =>                   1
    # 5th: 9   =>                   5
    # 6th: 11  =>           1 * 5 + 1
    # 10th: 19 =>           1 * 5 + 5
    # 30th: 99  =>          5 * 5 + 5
    # 31th: 111 => 1 * 25 + 1 * 5 + 1
    # Therefore, we can get a formula for the result.
    # N = a_k * 5^k + a_k-1 * 5^(k - 1) + ... + a_1 * 5^1 + a_0 * 5^0
    # All a_i are between 1 ~ 5
    # Therefore, we can calculate all a_i, and get the final result
    # TC: O(logn), SC: O(1)
    def findNumber(self, N : int) -> int:
        # code here
        seq = [1, 3, 5, 7, 9]
        ans = 0
        base = 1
        while N > 0:
            N -= 1
            ans += base * seq[N % 5]
            N //= 5
            base *= 10
        return ans