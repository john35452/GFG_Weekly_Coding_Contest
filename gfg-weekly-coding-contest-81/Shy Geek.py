#User function Template for python3

"""
Instructions - 

    1. 'shop' is object of class Shop.
    2. User 'shop.get(int i)' to enquire about the price
            of the i^th chocolate.
    3. Every chocolate in shop is arranged in non-decreasing order
            i.e. shop.get(i) <= shop.get(i + 1) for all 0 <= i < n - 1
"""

class Solution:
    # Version 1: Binary Search
    # Since the number of query is limited, we can store the result of previous queries.
    # TC: O(nlogn), SC: O(n)
    shop=Shop()
    def __init__(self,shop):
        self.shop=shop
        self.price = {}
    
    def getPrice(self, i):
        if i not in self.price:
            if len(self.price) < 50:
                self.price[i] = self.shop.get(i)
            else:
                return -1
        return self.price[i]
        
    def find(self,n,k):
        #code here
        ans = 0
        val = k
        r = n - 1
        while val > 0:
            l = 0
            while l < r:
                m = l + (r - l) // 2
                p = self.getPrice(m)
                if p > val:
                    r = m
                else:
                    l = m + 1
            l -= int(self.getPrice(l) > val)
            if l >= 0:
                ans += val // self.price[l]
                val %= self.price[l]
            else:
                break
            r = l
        return ans
            