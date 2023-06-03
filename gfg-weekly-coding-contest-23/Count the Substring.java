

//User function Template for Java

class Solution {
    // Version 1: BIT
    // Count the number of 1 minus number of 0
    // When the balance is k, for all the index with balance less than k
    // we can get a subarray with 1 more than 0.
    // TC: O(nlogn), SC: O(n)
    /*
    class BIT {
        int[] data;
        BIT(int n) {
            this.data = new int[n + 1];
        }
        
        void update(int index, int delta) {
            index += 1;
            while (index < this.data.length) {
                this.data[index] += delta;
                index += (index & -index);
            }
        }
        
        int prefix(int index) {
            index += 1;
            int sum = 0;
            while (index > 0) {
                sum += this.data[index];
                index -= (index & -index);
            }
            return sum;
        }
    }
    
    long countSubstring(String S){
        long ans = 0;
        int n = S.length();
        BIT tree = new BIT(2 * n + 1);
        int balance = 0;
        tree.update(n, 1);
        for (char c: S.toCharArray()) {
            if (c == '1') balance += 1;
            else balance -= 1;
            ans += tree.prefix(balance - 1 + n);
            tree.update(balance + n, 1);
        }
        return ans;
    }
    */
    
    // Version 2: Segment Tree
    // Same as version 1.
    // Just use different data structure for range sum
    // TC: O(nlogn), SC: O(n)
    /*
    class Node {
        int start;
        int end;
        int val;
        Node left;
        Node right;
        Node (int start, int end, int val, Node left, Node right) {
            this.start = start;
            this.end = end;
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }
    
    class SegmentTree {
        Node root;
        int[] data;
        SegmentTree(int[] data) {
            this.data = data;
            this.root = this.buildTree(0, data.length - 1);
        }
        
        Node buildTree(int left, int right) {
            if (left == right) {
                return new Node(left, right, this.data[left], null, null);
            } else {
                int mid = left + (right - left) / 2;
                Node l = this.buildTree(left, mid);
                Node r = this.buildTree(mid + 1, right);
                return new Node(left, right, l.val + r.val, l, r);
            }
        }
        
        int query(Node node, int left, int right) {
            if (left > right) return 0;
            if (node.start == left && node.end == right) {
                return node.val;
            } else {
                int mid = node.start + (node.end - node.start) / 2;
                if (left > mid) {
                    return this.query(node.right, left, right);
                } else if (right <= mid) {
                    return this.query(node.left, left, right);
                } else {
                    return this.query(node.left, left, mid) + this.query(node.right, mid + 1, right);
                }
            }
        }
        
        void update(Node node, int index, int delta) {
            if (node.start == index && node.end == index) {
                node.val += delta;
                this.data[index] += delta;
            } else {
                int mid = node.start + (node.end - node.start) / 2;
                if (index <= mid) {
                    this.update(node.left, index, delta);
                } else {
                    this.update(node.right, index, delta);
                }
                node.val = node.left.val + node.right.val;
            }
        }
    }
    
    
    long countSubstring(String S){
        long ans = 0;
        int n = S.length();
        int[] data = new int[2*n + 1];
        SegmentTree tree = new SegmentTree(data);
        int balance = 0;
        tree.update(tree.root, n, 1);
        for (char c: S.toCharArray()) {
            if (c == '1') balance += 1;
            else balance -= 1;
            ans += tree.query(tree.root, 0, balance - 1 + n);
            tree.update(tree.root, balance + n, 1);
        }
        return ans;
    }
    */
    
    // Version 3: Merge sort
    // Consider the balance result
    // arr: [0, 1, 1, 0, 1]
    // balance: [-1, 0, 1, 0, 1]
    // Any pair with (i, j) with balance[j] > balance[i], arr[i:j + 1] is a valid substring.
    // If the sort the numbers in reverse direction, pair (i, j) is an inversion pair.
    // So we can find the count of all inversion pair by using merge sort.
    // However, we also need to count the number of balance bigger than 0 which means the valid arr[:i + 1].
    // TC: O(nlogn), SC: O(n)
    long mergeSort(int[] arr, int left, int right) {
        if (left >= right) {
            return 0;
        } 
        int mid = left + (right - left) / 2;
        long inversionCount = 0;
        inversionCount += mergeSort(arr, left, mid);
        inversionCount += mergeSort(arr, mid + 1, right);
        
        int index = 0, i = left, j = mid + 1;
        int[] data = new int[right - left + 1];
        while (i <= mid && j <= right) {
            if (arr[i] >= arr[j]) {
                data[index] = arr[i];
                i += 1;
            } else {
                data[index] = arr[j];
                j += 1;
                inversionCount += (mid - i + 1);
            }
            index += 1;
        }
        
        while (i <= mid) {
            data[index] = arr[i];
            index += 1;
            i += 1;
        }
        
        while (j <= right) {
            data[index] = arr[j];
            index += 1;
            j += 1;
        }
        
        for (i = 0; i < right - left + 1; i++) {
            arr[left + i] = data[i];
        }
        return inversionCount;
    }
    
    long countSubstring(String S){
        long ans = 0;
        int n = S.length();
        int[] data = new int[n];
        int balance = 0;
        for (int i = 0; i < n; i++) {
            if (S.charAt(i) == '1') balance += 1;
            else balance -= 1;
            if (balance > 0) ans += 1;
            data[i] = balance;
        }
        
        ans += mergeSort(data, 0, n - 1);
        
        return ans;
    }
    
}