
/*
Instructions - 

    1. 'shop' is object of class Shop.
    2. User 'shop.get(int i)' to enquire about the price
            of the i^th chocolate.
    3. Every chocolate in shop is arranged in non-decreasing order
            i.e. shop.get(i) <= shop.get(i + 1) for all 0 <= i < n - 1
*/
class Solution{
    
    // Version 1: Binary Search
    // Since the number of query is limited, we can store the result of previous queries.
    // TC: O(nlogn), SC: O(n)
    unordered_map<int, int> price;
    Shop shop;
    
    public:
    Solution(Shop shop){
        // Constructor
        price.clear();
        this -> shop = shop;
    }
    
    long long find(int n, long k){
        // Return the number of chocolates Geek had
        // enjoyed out of 'n' chocolates availabe in the
        // 'shop'.
        long long val = k, ans = 0;
        int l = 0, r = n - 1;
        while (val > 0) {
            l = 0;
            while (l < r) {
                int m = l + (r - l) / 2;
                if (query(m) >= val) {
                    r = m;
                } else {
                    l = m + 1;
                }    
            }
            if (query(l) > val) l--;
            if (l >= 0) {
                ans += val / query(l);
                val %= query(l);    
            } else {
                break;
            }
            r = l;
        }
        return ans;
    }

    long long query(int i) {
        if (price.find(i) == price.end()) {
            if (price.size() < 50) {
                price[i] = shop.get(i);
            } else {
                return -1;
            }    
        }
        return price[i];
    }
};