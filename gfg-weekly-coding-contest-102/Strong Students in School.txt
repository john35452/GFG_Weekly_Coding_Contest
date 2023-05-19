#User function Template for python3

# Version 1: Sort
# TC: O(nlogn), SC: O(n)

def diffSum(n, m, arr): 
    # code here 
    arr.sort()
    bigger = sum(arr[-m:])
    smaller = sum(arr[:m])
    return bigger - smaller
    
#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__": 
	t = int(input())
	for _ in range(t):
		line = list(map(int, input().strip().split()))
		n = line[0]
		m = line[1]
		arr = list(map(int, input().strip().split()))
		print(diffSum(n,m,arr))
# } Driver Code Ends