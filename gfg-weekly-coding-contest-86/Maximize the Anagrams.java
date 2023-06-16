

//User function Template for Java

class Solution{
    // Version 1: Use treeset to store the frequency of each alphbet
    // TC: O(n + k log 26) = O(n + k), SC: O(n)
    /*
    public int maximumPossible(int n, int k, String s){
        // Code Here. 
        int[] fre = new int[26];
        for (int i = 0; i < n; i++) fre[s.charAt(i) - 'a']++;
        long M = (long)1e9 + 7;
        TreeSet<int[]> freTree = new TreeSet<int[]>((a, b) -> Arrays.compare(a, b));
        for (int i = 0; i < 26; i++) {
            freTree.add(new int[]{fre[i], i});
        }
        
        for (int i = 0; i < k; i++) {
            int[] item_max = freTree.pollLast();
            int[] item_min = freTree.pollFirst();
            if (item_max[0] - item_min[0] <= 1) {
                break;
            }
            fre[item_min[1]]++;
            fre[item_max[1]]--;
            item_max[0]--;
            item_min[0]++;
            freTree.add(item_max);
            freTree.add(item_min);
        }
        
        long fac[] = new long[n + 1];
        fac[0] = 1;
        for (int j = 1; j <= n; j++) {
            fac[j] = (fac[j - 1] * j) % M;
        }
        
        long ans = fac[n];
        for (int i = 0; i < 26; i++) {
            if (fre[i] > 1) {
                ans = (ans * bigpow(fac[fre[i]], M - 2, M)) % M;
            }
        }
        return (int)ans;
    }
    
    long bigpow(long a, long b, long M) {
        if (b == 0) return 1;
        long half = bigpow(a, b / 2, M);
        long res = (half * half) % M;
        if (b % 2 > 0) {
            res = (res * a) % M;
        }
        return res;
    }
    */
    
    // Version 2: Use Min and Max heap to get max and min frequency
    // TC: O(n + k log 26) = O(n + k), SC: O(n + 26) + O(n)
    public int maximumPossible(int n, int k, String s){
        // Code Here. 
        int[] fre = new int[26];
        for (int i = 0; i < n; i++) fre[s.charAt(i) - 'a']++;
        long M = (long)1e9 + 7;
        PriorityQueue<int[]> maxv = new PriorityQueue<int[]>((a, b) -> Integer.compare(b[0], a[0]));
        PriorityQueue<int[]> minv = new PriorityQueue<int[]>((a, b) -> Integer.compare(a[0], b[0]));
        
        for (int i = 0; i < 26; i++) {
            maxv.offer(new int[]{fre[i], i});
            minv.offer(new int[]{fre[i], i});
        }
        
        for (int i = 0; i < k; i++) {
            while (!maxv.isEmpty() && maxv.peek()[0] != fre[maxv.peek()[1]]) {
                maxv.poll();
            }
            
            while (!minv.isEmpty() && minv.peek()[0] != fre[minv.peek()[1]]) {
                minv.poll();
            }
            
            int[] item_max = maxv.poll();
            int[] item_min = minv.poll();
            if (item_max[0] - item_min[0] <= 1) {
                break;
            }
            fre[item_min[1]]++;
            fre[item_max[1]]--;
            item_max[0]--;
            item_min[0]++;
            maxv.offer(item_max);
            maxv.offer(item_min);
            minv.offer(item_max);
            minv.offer(item_min);
        }
        
        long fac[] = new long[n + 1];
        fac[0] = 1;
        for (int j = 1; j <= n; j++) {
            fac[j] = (fac[j - 1] * j) % M;
        }
        
        long ans = fac[n];
        for (int i = 0; i < 26; i++) {
            if (fre[i] > 1) {
                ans = (ans * bigpow(fac[fre[i]], M - 2, M)) % M;
            }
        }
        return (int)ans;
    }
    
    long bigpow(long a, long b, long M) {
        if (b == 0) return 1;
        long half = bigpow(a, b / 2, M);
        long res = (half * half) % M;
        if (b % 2 > 0) {
            res = (res * a) % M;
        }
        return res;
    }
}