#User function Template for python3

class Solution:    
    # Version 1: Consider maximum overlapping trains on each platform and each day
    # TC: O(nlogn), SC: O(n)
    '''
    def minimumPlatform2(self, arr, dep, days, platforms):
        import heapq
        n = len(arr)
        train = {}
        for i in range(n):
            if days[i] not in train:
                train[days[i]] = []
            train[days[i]].append([arr[i], dep[i]])
        
        res = 0
        for k in train:
            train[k].sort()
            #print(train[k])
            count = 0
            option = []
            for i in range(len(train[k])):
                while option and option[0] <= train[k][i][0]:
                    heapq.heappop(option)
                heapq.heappush(option, train[k][i][1])
                count = max(count, len(option))
            res = max(res, count)
        return res <= platforms
    '''
    
    # Version 2: Use diff array to consider overlapping
    # TC: O(n), SC: O(n)
    '''
    def minimumPlatform2(self, arr, dep, days, platforms):
        import heapq
        n = len(arr)
        train = {}
        for i in range(n):
            if days[i] not in train:
                train[days[i]] = [0]*2500
            train[days[i]][arr[i]] += 1
            train[days[i]][dep[i]] -= 1
            
        res = 0
        for k, diff in train.items():
            count = 0
            for i in range(2401):
                count += diff[i]
                res = max(res, count)
        return res <= platforms
    '''
    
    # Version 3: Sort all train event
    # TC: O(nlogn), SC: O(n)
    def minimumPlatform2(self, arr, dep, days, platforms):
        n = len(arr)
        train = []
        for i in range(n):
            train.append([days[i], arr[i], 1])
            train.append([days[i], dep[i], -1])
        train.sort()
        
        res = 0
        count = 0
        for d, t, v in train:
            count += v
            res = max(res, count)
        return res <= platforms
