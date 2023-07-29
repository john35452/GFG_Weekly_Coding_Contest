from typing import List



class Solution:
    # Version 1: Sort the query and count the result by scanning through the range
    # TC: O(qlogq + nq), SC: O(n + q)
    '''
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here
        from collections import Counter
        q = [Q[i] + [i] for i in range(num)]
        q.sort(key = lambda x:x[1])
        ans = [0]*num
        fre = Counter()
        j = N - 1
        for l, r, k, i in q:
            while j > r:
                fre[A[j]] += 1
                j -= 1
            
            while j < r:
                fre[A[j + 1]] -= 1
                j += 1
            
            while j >= l:
                fre[A[j]] += 1
                if fre[A[j]] == k:
                    ans[i] += 1
                j -= 1
        return ans
    '''
    
    # Version 2: Suffix sum of the number of same numbers
    # TC: O(n^2), SC: O(n^2)
    def solveQueries(self, N : int, num : int, A : List[int], Q : List[List[int]]) -> List[int]:
        # code here
        suffix = [[0]*(N + 1) for _ in range(N + 1)]
        for i in range(N):
            cnt = 0
            for j in range(i, N):
                if A[i] == A[j]:
                    cnt += 1
            suffix[i][cnt] += 1
            
        for i in range(N - 1, 0, -1):
            for j in range(N + 1):
                suffix[i - 1][j] += suffix[i][j]
        
        ans = []
        for l, r, k in Q:
            ans.append(suffix[l][k] - suffix[r + 1][k])
        return ans


