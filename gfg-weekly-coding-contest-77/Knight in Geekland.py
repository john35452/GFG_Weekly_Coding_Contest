#User function Template for python3

class Solution:
    # Version 1: BFS
    # Memorize scores for each step and add magical power
    # TC: O(mn), SC: O(nm)
    def knightInGeekland(self, arr, start):
        from collections import deque
        m = len(arr)
        n = len(arr[0])
        direction = [[2, 1], [1, 2]]
        queue = deque()
        queue.append(start)
        val = [arr[start[0]][start[1]]]
        arr[start[0]][start[1]] = -1
        while queue:
            size = len(queue)
            val.append(0)
            for _ in range(size):
                x, y = queue.popleft()
                sx = 1
                sy = 1
                for i in range(2):
                    for j in range(2):
                        for dx, dy in direction:
                            nx = x + sx * dx
                            ny = y + sy * dy
                            if 0 <= nx < m and 0 <= ny < n and arr[nx][ny] >= 0:
                                val[-1] += arr[nx][ny]
                                arr[nx][ny] = -1
                                queue.append([nx, ny])
                        sy *= -1
                    sx *= -1
        k = len(val)
        ans = 0
        for i in range(k):
            if i + val[i] < k:
                val[i] += val[i + val[i]]
            if val[i] > val[ans]:
                ans = i
        return ans
