class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class LinkedList:
    def __init__(self,data) -> None: #o(1)
        self.head = node(data)
        self.tail = self.head
        self.length = 1

   
    def append(self,data): #o(1)
        temp = node(data)
        self.tail.next = temp
        self.tail = temp
        self.length+=1
    def prepend(self,data): #o(1)
        temp = node(data)
        temp.next = self.head
        self.head = temp
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
            if(i == index-1):
                prev = curr
                next = curr.next
                curr.next = temp
                temp.next = next
                self.length+=1
                return
                
            curr = curr.next
        return   
    def delete(self,index):
        if(index<=self.length or index>0):
            print("Invalid Index")
            return
        if(index==0):
           temp = self.head.next
           self.head = temp
           self.length-=1
           return
        prev = self.head


        for i in range(self.length):
            if(i==index-1):
                toDelete = prev.next # item index to delete
                next = toDelete.next # the next item of item index to be deleted
                prev.next = next #previous item pointing ext item of item index to be deleted
                del toDelete
                self.length-=1
                return
            prev = prev.next


a = LinkedList(40)
a.append(402)
a.append (500)
a.prepend(2)
a.prepend(432)
a.insert(4,30)
a.delete(10)
a.print()

            
        