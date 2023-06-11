

class Solution {
    
    // Version 1: Count the state before the number
    // In this case, we can count the number of substring with even times odd numbers.
    // But it will also include the substring with 0 times odd numbers.
    // Therefore, we need to subtract subarrays without odd numbers.
    // TC: O(n), SC: O(1)
    /*
    public static long magicalSubarrays(int n, int[] arr) {
        // code here
        long ans = 0;
        int oddCount = 0;
        int[] fre = new int[2];
        fre[0] = 1;
        int evenCount = 0;
        int i = 0;
        for (int j = 0; j < n; j++) {
            if (arr[j] % 2 > 0) { 
                oddCount = oddCount + 1;
                i = j + 1;
            } else {
                evenCount += (j - i + 1);
            }
            ans += fre[oddCount % 2];
            fre[oddCount % 2]++;
        }
        return ans - evenCount;
    }
    */
    
    // Version 2: Store all odd number positions
    // We need to consider the situtation starting with 0 odd number and 1 odd number
    // TC: O(n), SC: O(n)
    public static long magicalSubarrays(int n, int[] arr) {
        // code here
        long ans = 0;
        List<Integer> pos = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (arr[i] % 2 > 0) pos.add(i);
        }
        pos.add(n);
        
        long cur = pos.get(0) + 1;
        for (int i = 1; i + 1< pos.size(); i += 2) {
            ans += cur * (pos.get(i + 1) - pos.get(i));
            cur += pos.get(i + 1) - pos.get(i);
        }
        
        cur = 0;
        for (int i = 0; i + 1 < pos.size(); i += 2) {
            ans += cur * (pos.get(i + 1) - pos.get(i));
            cur += pos.get(i + 1) - pos.get(i);
        }
        return ans;
    }
}
        