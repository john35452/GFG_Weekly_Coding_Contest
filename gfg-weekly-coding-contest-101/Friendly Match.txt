class Solution:
    # Version 1: Heap
    # Test on four cases
    # TC: O(nlogn), SC: O(n)
    '''
    def friendlyMatch(self, N, A):
        #code here
        import heapq
        ans = [0, 0]
        for i in range(2):
            pre = 0
            for j in range(2):
                data = [[], []]
                for k in A:
                    heapq.heappush(data[k % 2], -k)
                    
                player1 = player2 = 0
                p1 = i
                p2 = j
                while data[p1] or data[p2]:
                    if data[p1]:
                        player1 -= heapq.heappop(data[p1])
                        p1 ^= 1
                        done = False
                    if data[p2]:
                        player2 -= heapq.heappop(data[p2])
                        p2 ^= 1
                        done = False
                #print(i, j, player1, player2)
                if player2 > pre:
                    pre = player2
                    ans[i] = player1
        #print(ans)
        return max(ans)
    '''
    
    # Version 2: Sort
    # TC: O(nlogn), SC: O(n)
    def friendlyMatch(self, N, A):
        #code here
        ans = [0, 0]
        data = [[], []]
        for k in A:
            data[k % 2].append(k)
        data[0].sort(reverse=True)
        data[1].sort(reverse=True)
        for i in range(2):
            pre = 0
            for j in range(2):
                index = [0, 0]
                player1 = player2 = 0
                p1 = i
                p2 = j
                while index[p1] < len(data[p1]) or index[p2] < len(data[p2]):
                    if index[p1] < len(data[p1]):
                        player1 += data[p1][index[p1]]
                        index[p1] += 1
                        p1 ^= 1
                    if index[p2] < len(data[p2]):
                        player2 += data[p2][index[p2]]
                        index[p2] += 1
                        p2 ^= 1
                
                if player2 > pre:
                    pre = player2
                    ans[i] = player1

        return max(ans)