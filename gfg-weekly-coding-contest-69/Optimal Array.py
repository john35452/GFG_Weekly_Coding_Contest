from typing import List


class Solution:
    # Version 1: Max heap + Min heap
    # This approach can also be used for unsorted array
    # left heap store the first half numbers, right heap store the right half numbers
    # TC: O(nlogn), SC: O(n)
    '''
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        # code here
        import heapq
        left = []
        right = []
        left_sum = 0
        right_sum = 0
        ans = [0]*n
        for i in range(n):
            if len(left) == len(right):
                heapq.heappush(right, a[i])
                right_sum += a[i]
                item = heapq.heappop(right)
                right_sum -= item
                heapq.heappush(left, -item)
                left_sum += item
            else:
                heapq.heappush(left, -a[i])
                left_sum += a[i]
                item = -heapq.heappop(left)
                left_sum -= item
                heapq.heappush(right, item)
                right_sum += item
            mid = -left[0]
            ans[i] = mid * len(left) - left_sum + right_sum - mid * len(right)
        return ans
    '''
    
    # Version 2: Separate the left and right side
    # TC: O(n), SC: O(1)
    def optimalArray(self, n : int, a : List[int]) -> List[int]:
        # code here
        left_sum = total_sum = 0
        j = 0
        ans = [0]*n
        for i in range(n):
            total_sum += a[i]
            half = i // 2
            if i % 2 == 0:
                left_sum += a[j]
                j += 1
            ans[i] = a[half]*(half + 1) - left_sum + total_sum - left_sum - a[half] *(i - half)
        return ans

