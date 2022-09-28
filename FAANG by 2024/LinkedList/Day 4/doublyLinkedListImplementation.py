class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        self.prev = None 
class LinkedList:
    def __init__(self,data) -> None: #o(1)
        self.head = node(data)
        self.tail = self.head
        self.length = 1

   
    def append(self,data): #o(1)
        temp = node(data)
        prev = self.tail
        self.tail.next = temp
        self.tail = temp
        self.tail.prev = prev
        
        self.length+=1
    def prepend(self,data): #o(1)
        temp = node(data)
        temp.next = self.head
        self.head.prev = temp
        self.head = temp
        self.head.prev = None
        self.length+=1
            
    def print(self): #o(n) coz of looping elements/ traversing
        temp = self.head
        for i in range(self.length):
            print(temp.data)
            temp = temp.next

    def insert(self,index,data): #O(n) as traversing in the linked list to find the index
        if (self.length<=index):
            print("Index Not Found")
            return
        if (index==0):
            self.prepend(data)
            return
        if (index==self.length-1):
            self.append(data)
            return    

        temp =node(data)  
        curr = self.head
        for i in range(self.length):
            if(i == index):
                prev = curr.prev
                temp.next =curr
                temp.prev = prev
                self.length+=1
                
                
            curr = curr.next
        return   
    def delete(self,index): #If first index or last index then o(1) otherwise o(n) 
        if(index>=self.length or index<0):
            print("Invalid Index")
            return
        if(index==0): #o(1)
           temp = self.head.next
           temp.prev = None
           self.head = temp
           self.length-=1
           return
        if(index==self.length-1): #o(1)
            curr = self.tail
            self.tail = self.tail.prev
            self.tail.next = None 
            self.length-=1 
            return 
        curr = self.head


        for i in range(self.length): #o(n)
            if(i==index):

                prev = curr.prev
                next = curr.next
                prev.next = next
                self.length-=1
            curr = curr.next


a = LinkedList(40)
a.append(402)
a.append (500)
a.prepend(2)
a.prepend(432)
a.insert(4,30)
a.delete(50)
a.print()

            
        