#User function Template for python3
class Node:
    def __init__(self, num, next = None, prev = None):
        self.num = num
        self.next = next
        self.prev = prev
        self.data = []
    
class doublyLinkedList:
    def __init__(self):
        self.head = Node(None)
        self.head.next = self.head.prev = self.head
    
    def append(self, node):
        tail = self.head.prev
        tail.next = node
        node.prev = tail
        node.next = self.head
        self.head.prev = node
        
    def remove(self, node):
        prev = node.prev
        prev.next = node.next
        node.next.prev = prev
    
    def pop(self):
        item = self.head.next
        self.remove(item)
        return item
        
    def printList(self):
        current = self.head.next
        data = []
        while current != self.head:
            data.append(current.num)
            current = current.next
        return data
        
class Geekenger:
    
    # Version 1: LRU Cache
    # Use orderedDict as the doubly linked list
    # TC: O(|message|), SC: O(|message| * |number|) 
    '''
    def __init__(self,screenSize):
        # Constructor
        from collections import OrderedDict
        self.screenSize = screenSize
        self.data = OrderedDict()
        
    def send(self,number,message):
        # Send Message to "number"
        self.newMessage(number, message)
        
    def receive(self,number,message):
        # Receive message from "number"
        self.newMessage(number, message)
        
    def newMessage(self, number, message):
        if number in self.data:
            self.data.move_to_end(number, last=True)
        else:
            self.data[number] = []
            if len(self.data) > self.screenSize:
                self.data.popitem(last=False)
        self.data[number].append(message)
        
    def findLastKMessage(self, number,K):
        # Return list of lask K messages in the chat 
        # of "number" arranged in top to down order.
        if number not in self.data or len(self.data[number]) < K:
            return ["ERROR"]
        return self.data[number][-K:]
    '''
    
    # Version 2: HashMap + Doubly linked list
    # TC: O(|message|), SC: O(|message| * |number|) 
    def __init__(self,screenSize):
        # Constructor
        self.screenSize = screenSize
        self.data = {}
        self.list = doublyLinkedList()
        
    def send(self,number,message):
        # Send Message to "number"
        self.newMessage(number, message)
        
    def receive(self,number,message):
        # Receive message from "number"
        self.newMessage(number, message)
        
    def newMessage(self, number, message):
        if number in self.data:
            self.list.remove(self.data[number])
        else:
            self.data[number] = Node(number)
        self.list.append(self.data[number])
        if len(self.data) > self.screenSize:
            item = self.list.pop()
            self.data.pop(item.num)
        self.data[number].data.append(message)
        
    def findLastKMessage(self, number,K):
        # Return list of lask K messages in the chat 
        # of "number" arranged in top to down order.
        
        if number not in self.data or len(self.data[number].data) < K:
            return ["ERROR"]
        return self.data[number].data[-K:]