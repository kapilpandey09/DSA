class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Linklist:
    def __init__(self):
        self.head = None
        #number of node
        self.n = 0
    def __len__(self):
        return self.n
    def insert_head(self,value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
        self.n = self.n+1
    
    def __str__(self):
        curr = self.head
        result = ''
        while curr:
            result = result + str(curr.value)+ '->'
            curr = curr.next
        return result[:-2]
    
    def append(self,value):
        new_node = Node(value)
        if self.head == None:
            self.head =  new_node
            self.n = self.n +1
            return
        
        curr = self.head
        while curr.next:
            curr = curr.next
        
        curr.next = new_node
        self.n = self.n +1
    
    def insert_after(self,after,value):
        new_node  = Node(value)
        curr = self.head
        while curr != None:
            if curr.value == after:
                break
            curr = curr.next
        if curr!=None:
            print(curr.value)
            new_node.next = curr.next
            curr.next = new_node
            self.n = self.n +1
        else:
            return 'Item not found'
    
    def clear(self):
        self.head = None
        self.n = 0
    def delete_head(self):

        if self.head == None:
            return "eMPTY LINKLIST"
        self.head = self.head.next
        self.n -= 1


    def pop(self):

        curr = self.head
        if curr == None:
            return "Empty LinkList"

        if curr.next == None:
            return self.delete_head()
        
        while curr.next.next != None:
            curr = curr.next
        
        curr.next = None
        self.n -= 1

    def remove(self,value):
        new_node= Node(value)
        curr = self.head()
        if curr == None:
            return "Empty Link List"
        if curr.value == new_node:
            return self.delete_head()

        

        while curr.next!=None:
            if curr.next.value == new_node:
                break 
            curr = curr.next
        if curr.next == None:
            return 'Not Found'
        else:            
            curr.next = curr.next.next
    def search(self,item):
        curr = self.head()
        pos = 0
        
        while curr != None:
            if curr.value == item:
                return  pos
            curr = curr.next
            pos+=1
        return 'Not Fount'
    
    def __getitem__(self,index):
        curr = self.head
        pos = 0
        while curr != None:
            if pos == index:
                return curr.value
            curr = curr.next
            pos+=1
        return 'Index not range, index out of range'
            
    
            





L = Linklist() 
L.insert_head(1)
L.insert_head(2)
L.insert_head(3)
L.insert_head(4)
L.append(5)
print(L.delete_head())
print(L)
L.pop()
L.pop()
print(len(L))
print(L)