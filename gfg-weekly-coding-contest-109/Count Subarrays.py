#User function Template for python3
class Solution:
    
    # Version 1: Hashmap
    # pre[val][count]: The number of val with count times of X until now
    # TC: O(n), SC: O(n)
    '''
    def countSubarray(self,arr,N,X,K):
        # code here
        M = 10**9 + 7
        pos = {X:{0: 1}}
        count = 0
        ans = 0
        for i in range(N):
            count += int(arr[i] == X)
            if arr[i] in pos:
                key = count - K
                if key in pos[arr[i]]:
                    ans = (ans + pos[arr[i]][key]) % M
            else:
                pos[arr[i]] = {}
                
            if count not in pos[arr[i]]:
                pos[arr[i]][count] = 0
            pos[arr[i]][count] += 1
            #print(i, count, ans, pos)
        return ans
    '''
    
    # Verion 2: Sliding window
    # When we have k X, count the occurrence of non-X numbers from left.
    # Precede the right position until we meet X to count the number of valid substrings
    # TC: O(n), SC: O(n)
    def countSubarray(self,arr,N,X,K):
        # code here
        M = 10**9 + 7
        l = 0
        r = 0
        count = 0
        ans = 0
        while r < N:
            count += int(arr[r] == X)
            r += 1
            if count == K:
                pre = {}
                while arr[l] != X:
                    if arr[l] not in pre:
                        pre[arr[l]] = 0
                    pre[arr[l]] += 1
                    l += 1
                
                ans = (ans + 1) % M
                while r < N and arr[r] != X:
                    if arr[r] in pre:
                        ans = (ans + pre[arr[r]]) % M
                    r += 1
                l += 1
                count -= 1
        return ans
    