class node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
class Stacks:
    def __init__(self,data=None) -> None:
        self.top = node(data)
        self.length = 0
        if data!=None:
            self.length+=1
    def push(self,data):
        if self.top == None:
            self.top = node(data)
            self.length+=1
            return
        temp = node(data)
        top = self.top
        self.top = temp
        self.top.next= top   
        self.length+=1
        return
    def pop(self):
        if self.length==0:
            print("stack is empty")
            return
        if self.length==1:
            self.top.data = None
            self.length-=1
            return
                
        top = self.top
        next = top.next
        top.next = None
        del top
        self.top = next      
        self.length-=1     
    def lookup(self):
        return self.top.data


s = Stacks(1)

s.push(4)
s.push(9)

print(s.lookup())
