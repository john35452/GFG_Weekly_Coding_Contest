from typing import List

class BIT:
    
    def __init__(self, n):
        self.data = [0]*(n + 1)
    
    def update(self, index, delta):
        index += 1
        while index < len(self.data):
            self.data[index] += delta
            index += (index & -index)
        
    def query(self, index):
        res = 0
        index += 1
        while index > 0:
            res += self.data[index]
            index -= (index & - index)
        return res

class Node:
    def __init__(self, val, start, end, left = None, right = None):
        self.val = val
        self.start = start
        self.end = end
        self.left = left
        self.right = right
        
class segmentTree:
    def __init__(self, data):
        self.data = data
        self.root = self.buildTree(0, len(data) - 1)
    
    def buildTree(self, i, j):
        if i == j:
            return Node(self.data[i], i, j)
        else:
            m = i + (j - i) // 2
            left = self.buildTree(i, m)
            right = self.buildTree(m + 1, j)
            return Node(left.val + right.val, i, j, left, right)
    
    def update(self, i, delta, node):
        if node.start == i and node.end == i:
            node.val += delta
            self.data[i] += delta
        else:
            mid = node.start + (node.end - node.start) // 2
            if i <= mid:
                self.update(i, delta, node.left)
            else:
                self.update(i, delta, node.right)
            node.val = node.left.val + node.right.val
    
    def query(self, i, j, node):
        if node.start == i and node.end == j:
            return node.val
        else:
            mid = node.start + (node.end - node.start) // 2
            if i > mid:
                return self.query(i, j, node.right)
            elif j <= mid:
                return self.query(i, j, node.left)
            else:
                return self.query(i, mid, node.left) + self.query(mid + 1, j, node.right)

class segmentTree_array:
    def __init__(self, s):
        self.data = [[0]*26 for _ in range(4 * len(s))]
        self.buildTree(s, 0, len(s) - 1, 0)
    
    def buildTree(self, s, i, j, index):
        if i == j:
            self.data[index][ord(s[i]) - ord('a')] = 1
        else:
            m = i + (j - i) // 2
            self.buildTree(s, i, m, 2 * index + 1)
            self.buildTree(s, m + 1, j, 2 * index + 2)
            for k in range(26):
                self.data[index][k] = self.data[2 * index + 1][k] + self.data[2 * index + 2][k] 
    
    def update(self, c, i, delta, start, end, index):
        seq = ord(c) - ord('a')
        if start == i and end == i:
            self.data[index][seq] += delta;
        else:
            mid = start + (end - start) // 2
            if i <= mid:
                self.update(c, i, delta, start, mid, 2 * index + 1)
            else:
                self.update(c, i, delta, mid + 1, end, 2 * index + 2)
            self.data[index][seq] =  self.data[2 * index + 1][seq] + self.data[2 * index + 2][seq]
    
    def query(self, i, j, start, end, index):
        if start == i and end == j:
            return [self.data[index][k] for k in range(26)]
        else:
            mid = start + (end - start) // 2
            if j <= mid:
                return self.query(i, j, start, mid, 2 * index + 1)
            elif i > mid:
                return self.query(i, j, mid + 1, end, 2 * index + 2)
            else:
                left = self.query(i, mid, start, mid, 2 * index + 1)
                right = self.query(mid + 1, j, mid + 1, end, 2 * index + 2)
                for k in range(26):
                    left[k] += right[k]
                return left
                
class Solution:
    # Version 1: Fenwick tree
    # Use Fenwick tree to store the number of each alphbet in the array
    # TC: O(q * 26 * logn) = O(qlogn), SC: O(26n) = O(n)
    '''
    def easyTask(self,n,s,q,queries) -> List[int]:
        # code here
        fre = [BIT(n) for _ in range(26)]
        s_char = list(s)
        for i in range(n):
            c = ord(s[i]) - ord('a')
            fre[c].update(i, 1)
        
        ans = []
        for i in range(q):
            if queries[i][0] == "1":
                index, char = int(queries[i][1]), queries[i][2]
                c = ord(s_char[index]) - ord('a')
                fre[c].update(index, -1)
                new_c = ord(char) - ord('a')
                fre[new_c].update(index, 1)
                s_char[index] = char
            else:
                left, right, k = [int(_) for _ in queries[i][1:]]
                count = 0
                for j in range(25, -1, -1):
                    occur = (fre[j].query(right) - fre[j].query(left - 1))
                    count += occur
                    if count >= k:
                        ans.append(chr(ord('a') + j))
                        break
        return ans
    '''
    
    # Version 2: Segment tree(TLE)
    # Use segment tree to store the number of each alphbet in the array
    # TC: O(26 * (nlogn + qlogn)) = O(nlogn + qlogn), SC: O(26n) = O(n)
    '''
    def easyTask(self,n,s,q,queries) -> List[int]:
        # code here
        fre_c = [[0]*n for _ in range(26)]
        s_char = list(s)
        for i in range(n):
            c = ord(s[i]) - ord('a')
            fre_c[c][i] += 1
        fre = [segmentTree(fre_c[i]) for i in range(26)]
        
        ans = []
        for i in range(q):
            if queries[i][0] == "1":
                index, char = int(queries[i][1]), queries[i][2]
                if s_char[index] != char:
                    c = ord(s_char[index]) - ord('a')
                    fre[c].update(index, -1, fre[c].root)
                    new_c = ord(char) - ord('a')
                    fre[new_c].update(index, 1, fre[new_c].root)
                    s_char[index] = char
            else:
                left, right, k = [int(queries[i][j]) for j in range(1, 4)]
                count = 0
                for j in range(25, -1, -1):
                    count += fre[j].query(left, right, fre[j].root);
                    if count >= k:
                        ans.append(chr(ord('a') + j))
                        break
        return ans
    '''
    
    # Version 3: Array Segment tree
    # Use segment tree to store the number of each alphbet in the array
    # TC: O(nlogn + qlogn), SC: O(26n) = O(n)
    def easyTask(self,n,s,q,queries) -> List[int]:
        # code here
        s = list(s)
        tree = segmentTree_array(s)
        ans = []
        for i in range(q):
            if queries[i][0] == "1":
                index, char = int(queries[i][1]), queries[i][2]
                if s[index] != char:
                    tree.update(s[index], index, -1, 0, n - 1, 0)
                    tree.update(char, index, 1, 0, n - 1, 0)
                    s[index] = char
            else:
                left, right, k = [int(queries[i][j]) for j in range(1, 4)]
                data = tree.query(left, right, 0, n - 1, 0)
                count = 0
                for j in range(25, -1, -1):
                    count += data[j];
                    if count >= k:
                        ans.append(chr(ord('a') + j))
                        break
        return ans
                