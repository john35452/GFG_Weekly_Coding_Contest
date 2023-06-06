
from typing import List


class Solution:
    # Version 1: Check location
    # The testcase include some weird testcase, so this code gets WA.
    # TC: O(1), SC: O(1)
    '''
    def minimumThorns(self, n : int, m : int, geek : List[int], geekina : List[int]) -> int:
        # code here
        dx = abs(geek[0] - geekina[0])
        dy = abs(geek[1] - geekina[1])
        if max(dx, dy) == 1 and min(dx, dy) == 0:
            return -1
        
        ans = [4, 4]
        point = [geek, geekina]
        for i in range(2):
            if point[i][0] == 1 or point[i][0] == n:
                ans[i] -= 1
            if point[i][1] == 1 or point[i][1] == m:
                ans[i] -= 1
        return min(ans)
    '''

    # Version 2: Check the surrunding
    # TC: O(1), SC; O(1)
    def minimumThorns(self, n : int, m : int, geek : List[int], geekina : List[int]) -> int:
        # code here
        dx = abs(geek[0] - geekina[0])
        dy = abs(geek[1] - geekina[1])
        if max(dx, dy) == 1 and min(dx, dy) == 0:
            return -1
        
        ans = [0, 0]
        point = [geek, geekina]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        for i in range(2):
            for dx, dy in direction:
                nx = point[i][0] + dx
                ny = point[i][1] + dy
                if 1 <= nx <= n and 1 <= ny <= m:
                    ans[i] += 1
        return min(ans)