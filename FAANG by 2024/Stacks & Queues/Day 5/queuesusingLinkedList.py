class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class Queues:
    def __init__(self,data=None) -> None:
        self.first = None
        self.last = self.first
        self.length= 0
        if data!=None:
            self.first = node(data)
            self.last = self.first
            self.length+=1

    def enqueue(self,data):
        if self.first == None:
            self.first = node(data)
            self.last = self.first
            self.length+=1
            return
        temp = node(data)
        self.last.next = temp
        self.last = temp 
        self.length+=1
        return
    def dequeue(self):
        if (self.first==None):
            print("Queue is empty")
            return
        temp = self.first.next
        self.first = temp
        self.length-=1
        return                   
    def lookup(self):
        if (self.first==None):
            return "Empty queue"
        return self.first.data


qu = Queues()
qu.enqueue(1)
qu.enqueue(2)  
qu.enqueue(3)
qu.dequeue()
qu.dequeue()
qu.dequeue()
qu.enqueue(2)  
qu.enqueue(3)
qu.enqueue(9)  
qu.enqueue(6)
print(qu.lookup())      