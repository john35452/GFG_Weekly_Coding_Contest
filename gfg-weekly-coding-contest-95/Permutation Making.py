#User function Template for python3

class Solution:
    # Version 1: Greedy and Math
    # Consider the possible values after mod
    # k = 5
    # 5 % 4 = 1
    # 5 % 3 = 2
    # 5 % 2 = 1
    # 5 % 1 = 0
    
    # k = 6
    # 6 % 5 = 1
    # 6 % 4 = 2
    # 6 % 3 = 0
    # 6 % 2 = 0
    # 6 % 1 = 0
    
    # k = 7
    # 7 % 6 = 1
    # 7 % 5 = 2
    # 7 % 4 = 3
    # 7 % 3 = 1
    # 7 % 2 = 1
    # 7 % 1 = 0
    
    # We can observe that the possible value after mod is k / 2 - 1
    # Since we would like to minimize the cost, we should choose numbers between 1~n first.
    # Then, we can find the missing values from the biggest number.
    # TC: O(nlogn), SC: O(n)
    def makePermutation(self, n, arr):
        # code here
        arr.sort()
        used = [False]*(n + 1)
        for i in range(n):
            if arr[i] <= n:
                if not used[arr[i]]:
                    used[arr[i]] = True
                    arr[i] = -1
            else:
                break
        
        #print(arr)
        res = 0
        j = n
        for i in range(n - 1, -1, -1):
            if arr[i] < 0:
                continue
            while j > 0 and used[j]:
                j -= 1
            #print(i, j, used)
            if arr[i] > j:
                half = ((arr[i] + 1) // 2) - 1
                if half < j:
                    return -1
                else:
                    res += 1
                    used[j] = True
            elif arr[i] < j:
                return -1
        return res
            
        
        
        