#User function Template for python3
class Solution:
    # Version 1: Greedy
    # Sort by start time, and choose the earliest deadline friends
    # TC: O(nlogn + max(end) * logn), SC: O(n)
    def friends(self, N, K, start, end): 
        # code here
        import heapq
        friend = [[start[i], end[i], i] for i in range(N)]
        friend.sort()
        ans = 0
        option = []
        current = friend[0][0]
        i = 0
        while option or i < N:
            while option and option[0] < current:
                heapq.heappop(option)
            while i < N and friend[i][0] <= current:
                heapq.heappush(option, friend[i][1])
                i += 1
            count = 0
            while option and count < K:
                item = heapq.heappop(option)
                ans += 1
                count += 1   
            current += 1
        return ans
