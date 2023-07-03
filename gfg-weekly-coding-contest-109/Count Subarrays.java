

class Solution{
    // Version 1: Hashmap
    // pre[val][count]: The number of val with count times of X until now
    // TC: O(n), SC: O(n)
    /*
    public int countSubarray(int arr[], int n, int X, int K){
        // Code here. 
        Map<Integer, Map<Integer, Integer>> pre = new HashMap<>();
        pre.put(X, new HashMap<Integer, Integer>());
        pre.get(X).put(0, 1);
        long ans = 0;
        int M = (int)Math.pow(10, 9) + 7;
        int current = 0;
        for (int i = 0; i < n; i++) {
            int val = arr[i];
            if (val == X) current++;
            Map<Integer, Integer> f;
            if (pre.containsKey(val)) {
                f = pre.get(val);
                if (current >= K && f.containsKey(current - K)) {
                    ans = (ans + f.get(current - K)) % M;
                }
            } else {
                f = new HashMap<Integer, Integer>();
            }
            f.put(current, f.getOrDefault(current, 0) + 1);
            pre.put(val, f);
        }
        return (int)ans;
    }
    */
    
    // Verion 2: Sliding window
    // When we have k X, count the occurrence of non-X numbers from left.
    // Precede the right position until we meet X to count the number of valid substrings
    // TC: O(n), SC: O(n)
    public int countSubarray(int arr[], int n, int X, int K){
        int ans = 0;
        int count = 0;
        int l = 0, r = 0;
        int M = (int)Math.pow(10, 9) + 7;
        Map<Integer, Integer> pre = new HashMap<>();
        while (r < n) {
            if (arr[r] == X) count++;
            r++;
            if (count == K) {
                pre.clear();
                while(arr[l] != X) {
                    pre.put(arr[l], pre.getOrDefault(arr[l], 0) + 1);
                    l++;
                }
                
                ans = (ans + 1) % M;
                while(r < n && arr[r] != X) {
                    if (pre.containsKey(arr[r])) {
                        ans = (ans + pre.get(arr[r])) % M;
                    }
                    r++;
                }
                l++;
                count--;
            }
        }
        return ans;
    }
    
}