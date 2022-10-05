class stack:
    def __init__(self) -> None:
        
        self.container = []
    def lookup(self):
        if self.container == []:
            print( "Stack is Empty")
            return
        return self.container[len(self.container)-1]

    def push(self,data):
        self.container.append(data)
    def pop(self):
        if self.container == []:
            return False
        self.container.pop()
st = stack()
st.push(4)
st.push(5)
st.push(6)
print(st.lookup())
          