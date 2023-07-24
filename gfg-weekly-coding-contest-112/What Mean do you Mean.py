from typing import List


class Solution:
    # Version 1: Two sum
    # TC: O(nlogn), SC: O(1)
    '''
    def IsMean(self, n : int, k : int, x : int, arr : List[int]) -> bool:
        # code here
        arr.sort()
        total = sum(arr)
        target_sum = x * n
        l = 0
        r = n - 1
        while l < r:
            sums = (arr[l] + arr[r])*(k - 1) + total
            if sums == target_sum:
                return True
            elif sums > target_sum:
                r -= 1
            else:
                l += 1
        return False
    '''
    
    # Version 2: Another two sum
    # TC: O(n), SC: O(n)
    def IsMean(self, n : int, k : int, x : int, arr : List[int]) -> bool:
        # code here
        target = x * n - sum(arr)
        pre = set()
        for val in arr:
            remain = target - val * (k - 1)
            if remain in pre:
                return True
            pre.add(val * (k - 1))
        return False

