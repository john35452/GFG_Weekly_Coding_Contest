

//User function Template for Java

class Sol
{
    // Version 1: Sort
    // TC: O(nlogn), SC: O(n)
    public static int diffSum(int n,int m,int arr[])
    {
        //code here.
        Arrays.sort(arr);
        long Group1 = 0, Group2 = 0;
        for (int i = 0; i < m; i++) {
            Group1 += arr[i];
            Group2 += arr[n - i - 1];
        }
        return (int)(Group2 - Group1);
    }
}