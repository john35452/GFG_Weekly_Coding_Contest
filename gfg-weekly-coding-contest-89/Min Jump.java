

//User function Template for Java

class Solution{
    // Version 1: Binary Search
    // Find the minimum power to reach the last index
    // TC: O(nlogn), SC: O(1)
    /*
    static int minJump(int arr[], int n){
        int l = 1;
        int r = n;
        while (l < r) {
            int m = l + (r - l) / 2;
            if (check(m, arr)) {
                r = m;
            } else {
                l = m + 1;
            }
        }
        return l;
    }
    
    static boolean check(int power, int arr[]) {
        int farest = power;
        for (int i = 0; i < arr.length; i++) {
            if (i > farest) return false;
            if (arr[i] % 2 == 0 || arr[i] % 3 == 0) {
                farest = Math.max(farest, i + power);
            }
        }
        return true;
    }
    */
    
    // Version 2: Check the maximum jump between possible locations
    // TC: O(n), SC: O(1)
    static int minJump(int arr[], int n){
        int last = 0;
        int power = 1;
        for (int i = 0; i < n; i++) {
            if (arr[i] % 2 == 0 || arr[i] % 3 == 0) {
                power = Math.max(power, i - last);
                last = i;
            }
        }
        return power;
    }
}