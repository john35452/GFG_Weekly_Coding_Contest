from typing import List


class Solution:
    # Version 1: BFS
    # TC: O(mn), SC: O(mn)
    def possiblePath(self, n : int, m : int, grid : List[List[int]]) -> int:
        # code here
        from collections import deque
        dis = [[float('inf')]*m for _ in range(n)]
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        queue = deque()
        queue.append([0, 0])
        dis[0][0] = 0
        while queue:
            x, y = queue.popleft()
            power = grid[x][y] == 2
            for dx, dy in direction:
                nx = x + dx
                ny = y + dy
                if 0 <= nx < n and 0 <= ny < m and dis[nx][ny] > dis[x][y] + 1:
                    if grid[nx][ny] == 1:
                        if power:
                            dis[nx][ny] = dis[x][y] + 1
                            queue.append([nx, ny])
                    else:
                        dis[nx][ny] = dis[x][y] + 1
                        queue.append([nx, ny])
        return dis[-1][-1] if dis[-1][-1] != float('inf') else -1
        

