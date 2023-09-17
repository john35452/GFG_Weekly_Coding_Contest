#User function Template for python3

class Solution():
    
    # Version 1: Group and sort
    # TC: O(nlogn), SC: O(n)
    '''
    def check(self, D, N, A):
        #your code goes here
        used = set()
        for i in range(N):
            if i not in used:
                group_index = set()
                group_val = []
                cur = i
                while cur not in group_index:
                    used.add(cur)
                    group_index.add(cur)
                    group_val.append(A[cur])
                    cur = (cur + D) % N
                group_index = sorted(group_index)
                group_val.sort()
                for j in range(len(group_index)):
                    A[group_index[j]] = group_val[j]
        for i in range(1, N):
            if A[i] < A[i - 1]:
                return False
        return True
    '''
    
    # Version 2: Use gcd to know the size of each step
    # TC: O(nlogn), SC: O(n)
    def check(self, D, N, A):
        #your code goes here
        import math
        g = math.gcd(D, N)
        if g > 0:
            for i in range(g):
                group_data = []
                for j in range(i, N, g):
                    group_data.append(A[j])
                group_data.sort()
                for j in range(N // g):
                    A[i + j * g] = group_data[j]
        for i in range(1, N):
            if A[i] < A[i - 1]:
                return False
        return True
        