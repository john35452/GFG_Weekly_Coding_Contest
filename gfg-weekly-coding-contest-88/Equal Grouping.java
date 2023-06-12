

//User function Template for Java

class Solution{
    
    // Version 1: Stack
    // Convert numbers between 2^k ~ 2^(k+1) - 1 to 2^k.
    // Pop numbers when we meet a different numbers.
    // TC: O(nlogn), SC: O(n)
    /*
    public int evenGrouping(int n, int a[]){
        // Code Here.
        for (int i = 0; i < n; i++) {
            long base = 1;
            while (base <= a[i]) base <<= 1;
            a[i] = (int)(base / 2);
        }
        
        ArrayList<Integer> stack = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (stack.isEmpty() || a[i] == stack.get(stack.size() - 1)) {
                stack.add(a[i]);
            } else {
                int count = 0;
                int j = stack.size() - 1;
                while (j >= 0) {
                    if (Integer.compare(stack.get(j), stack.get(stack.size() - 1)) == 0) {
                        count++;
                        j--;
                    } else {
                        break;
                    }
                }
                if (count >= 2) {
                    count = 2 * (count / 2);
                    for (j = 0; j < count; j++) stack.remove(stack.size() - 1);
                }
                stack.add(a[i]);
            }
        }
        int count = 0;
        int j = stack.size() - 1;
        while (j >= 0) {
            if (Integer.compare(stack.get(j), stack.get(stack.size() - 1)) == 0) {
                count++;
                j--;
            } else {
                break;
            }
        }
        if (count >= 2) {
            count = 2 * (count / 2);
            for (j = 0; j < count; j++) stack.remove(stack.size() - 1);
        }
        return stack.size();
    }
    */
    
    // Version 2: Improved version 1
    // TC: O(n), SC: O(n)
    public int evenGrouping(int n, int a[]){
        // Code Here.
        for (int i = 0; i < n; i++) {
            a[i] = (int)(Math.log(a[i]) / Math.log(2));
        }
        
        Stack<Integer> stack = new Stack<>();
        for (int i = 0; i < n; i++) {
            if (stack.isEmpty()) {
                stack.add(a[i]);
            } else {
                if (stack.peek() == a[i]) {
                    stack.pop();
                } else {
                    stack.push(a[i]);
                }
            }
        }
        return stack.size();
    }
}