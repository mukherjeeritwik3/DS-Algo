
# Hash Table with collison s Handled

class HashTable:
    def __init__(self, size) -> None:
        self.size = size
        self.data = [[] for x in range(self.size)]

    def hash(self,key): # o(n) for creating hash code
        hash = 0
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        
        return hash

    def get(self,key): #o(1)
        hash = self.hash(key)
        for i in range(len(self.data[hash])):
            if (self.data[hash][i][0]==key):
                return self.data[hash][i][1]
        return None        
            
    def set(self,key,data): #o(n) worst to search the inner array
        hash = self.hash(key)
        for i in range(len(self.data[hash])):
            if (self.data[hash][i][0]==key):
                self.data[hash][i] = [key,data]
                return True
        self.data[hash].append([key,data])

    def keys(self):
        keyArr = []

        for i in range(len(self.data)):
            if self.data[i] == []:
                continue
            else:
                for j in range(len(self.data[i])):
                    keyArr.append(self.data[i][j][0])  
        return keyArr          

myHashTable = HashTable(20);
myHashTable.set('grapes', 10000)
print(myHashTable.get('grapes'))
myHashTable.set('apples', 9)
print(myHashTable.get('apples'))


print(myHashTable.keys())