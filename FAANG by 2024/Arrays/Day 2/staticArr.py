
import numpy as np

class Arrays:
    # Constructor With parameters specifying the length of the array and properties such as length, index, and arrayData
    def __init__(self,length) -> None: 
        self.length = length
        self.indexFilled = None #Tracks which index has data strating with None datatype
        self.data = np.empty(self.length,dtype=object)
    
    # push operation to add new eleemnts to the end of the array     
    def push(self,item):
        if (self.length==self.indexFilled):
            print("Array is Full")
            return False
        if(self.indexFilled==None):
           self.indexFilled=0 #setting to 0 in order start filling and counting index
           self.data[self.indexFilled] =item
           return True   
        self.indexFilled+=1     
        self.data[self.indexFilled] =item
        
        return True
    
    # get operation to get data by index    
    def get(self,index):
        if (index>self.length):
            print("Index out of Bound")
            return False
        return self.data[index]
    
    # pop operation to delete the data from the last    
    def pop(self):
        if(self.indexFilled==0):
            print("Nothing to delete from last")
            return False
        self.data[self.indexFilled] = None
        self.indexFilled-=1
        return True
    
    #delete and shift operation remove ith element from the array    
    def delete(self,index):
        if (index>self.indexFilled):
            print("Index Out of Bound")
            return False
        self.shift(index)
        self.pop()
        return True
    def shift(self,index):
        for i in range(index,self.indexFilled):
            self.data[i] = self.data[i+1]

    # replacing data by indexes
    def replace(self,index,newData):
        if(self.indexFilled<index):
            print("Invalid index given")
            return False
        self.data[index] = newData
        return True            

newArray = Arrays(5)
newArray.push(1)
newArray.push(2)
newArray.push(3)
newArray.push(4)
newArray.push(5)
newArray.pop()
newArray.replace(2,9)



print(newArray.indexFilled)
print(newArray.data)

