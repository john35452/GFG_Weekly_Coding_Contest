from typing import List


class Solution:
    # Version 1: Store all changing point and use diff array
    # TC: O(nlogn), SC: O(n)
    '''
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        # code here
        if k > n:
            return -1
        point = set()
        diff = {}
        for x, y in intervals:
            point.add(x)
            point.add(y)
            point.add(y + 1)
            if x not in diff:
                diff[x] = 0
            diff[x] += 1
            if y + 1 not in diff:
                diff[y + 1] = 0
            diff[y + 1] -= 1
        
        point = sorted(point)
        current = 0
        ans = -1
        for t in point:
            current += diff.get(t, 0)
            #print(t, current)
            if current >= k:
                ans = t
        return ans
    '''
    
    # Version 2: Improved version 1
    # Store two points for each interval
    # TC: O(nlogn), SC: O(n)
    def powerfullInteger(self, n : int, intervals : List[List[int]], k : int) -> int:
        # code here
        if k > n:
            return -1
        diff = {}
        for x, y in intervals:
            if x not in diff:
                diff[x] = 0
            diff[x] += 1
            if y + 1 not in diff:
                diff[y + 1] = 0
            diff[y + 1] -= 1
        
        current = 0
        ans = -1
        for t in sorted(diff.keys()):
            if diff[t] > 0:
                current += diff[t]
                if current >= k:
                    ans = t
            else:
                if current >= k:
                    ans = t - 1
                current += diff[t]
        return ans
        

