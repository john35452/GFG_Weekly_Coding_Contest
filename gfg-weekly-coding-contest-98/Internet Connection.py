#User function Template for python3

from typing import List

class Solution:
    # Version 1: BFS
    # TC: O(n^2), SC: O(n^2)
    '''
    def internetCoverage(self, rang : int, n : int, wifi : List[List[int]]) -> bool:
        current = set()
        for i in range(n):
            for j in range(n):
                if wifi[i][j] > 0:
                    current.add((i, j))
        direction =[[1, 0], [1, -1], [1, 1], [0, 1], [0, -1],[-1, 0],[-1, 1], [-1, -1]]
        cover = set()
        for _ in range(rang):
            nextStep = set()
            cover.update(current)
            for x, y in current:
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in cover:
                        nextStep.add((nx, ny))
            current = nextStep
        return len(cover) == n * n
    '''
    
    # Version 2: Inplace
    # We still need the space for each round of expansion.
    # TC: O(n^2), SC: O(n)
    def internetCoverage(self, rang : int, n : int, wifi : List[List[int]]) -> bool:
        current = set()
        for i in range(n):
            for j in range(n):
                if wifi[i][j] > 0:
                    current.add((i, j))
        direction =[[1, 0], [1, -1], [1, 1], [0, 1], [0, -1],[-1, 0],[-1, 1], [-1, -1]]
        count = 0
        for _ in range(rang):
            nextStep = set()
            count += len(current)
            for x, y in current:
                wifi[x][y] = 1
            for x, y in current:
                for dx, dy in direction:
                    nx = x + dx
                    ny = y + dy
                    if 0 <= nx < n and 0 <= ny < n and wifi[nx][ny] == 0:
                        nextStep.add((nx, ny))
            current = nextStep
        return count == n * n
        