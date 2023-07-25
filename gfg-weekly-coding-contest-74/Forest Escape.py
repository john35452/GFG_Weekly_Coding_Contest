#User function Template for python3

from typing import List

class Solution:
    # Version 1: BFS
    # TC: O(mn), SC: O(m + n)
    def escapeForest(self, n : int, m : int, grid : List[List[int]]) -> bool:
        from collections import deque
        queue = deque()
        people = None
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "X":
                    queue.append([i, j, 0])
                elif grid[i][j] == "M":
                    people = [i, j, 1]
        
        queue.append(people)
        direction = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while queue:
            size = len(queue)
            for _ in range(size):
                x, y, state = queue.popleft()
                if state == 1:
                    if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                        return True
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < m:
                        if grid[nx][ny] != "X":
                            if state == 0:
                                grid[nx][ny] = "X"
                                queue.append([nx, ny, state])
                            elif grid[nx][ny] != "M":
                                grid[nx][ny] = "M"
                                queue.append([nx, ny, state])
        return False

