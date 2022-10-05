# Binary Search Tree Implementation 

class node:
    def __init__(self,data) -> None:
        self.data = data
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self,data):
        if self.root == None:
            self.root = node(data)
            return
        temp = self.root
        newVal = node(data)
        while(True):
            if(data>temp.data):
                if (temp.right == None):
                    temp.right = newVal
                    return
                if (temp.right.data == data):
                    print("Dupblicates Not Allowed")
                    return    
                else:
                    temp = temp.right
                    continue  
            if(data<temp.data):
                if (temp.left == None):
                    temp.left = newVal
                    return
                if (temp.left.data == data):
                    print("Dupblicates Not Allowed")
                    return    
                else:
                    temp = temp.left
                    continue
    def lookup(self,data):
        temp = self.root
        if self.root.data == data:
            return True
        while(True):
            if(data>temp.data):
                if(temp.right==None):
                    return False
                temp = temp.right
                if(temp.data==data):
                    return True
            if(data<temp.data):
                if(temp.left==None):
                    return False
                temp = temp.left
                if(data==temp.data):
                    return True         

    def remove(self, value):
 
        #Search node
        current_node = self.root
        parent_node = None
        direction = None
        left_node = None
 
        while True:
            if current_node.value < value:
                parent_node = current_node
                direction = 'right'
                current_node = current_node.right
 
            elif current_node.value > value:
                parent_node = current_node
                direction = 'left'
                current_node = current_node.left
 
            else:
                #Find value!!
 
                #Check if it is a leaf
                if self._leaf(current_node):
                    if direction == 'left':
                        parent_node.left = None
                        
                    else:
                        parent_node.right = None
                    break
                    
 
                #Check if it has a child
                elif self._one_child(current_node):
 
                    if direction == 'left':
                        if self._have_left_child(current_node):
                            parent_node.left = current_node.left
                        else:
                            parent_node.left = current_node.right
                    else:
                        if self._have_left_child(current_node):
                            parent_node.right = current_node.left
                        else:
                            parent_node.right = current_node.right
 
                    break
                    
 
                #Check if it has 2 children
                elif self._2_children(current_node):
                    left_node = current_node.left
                    print(left_node.value, 'left')
                    print(parent_node.value, 'parent')
                    current_node = current_node.right
 
                    if self._leaf(current_node):
                        replace_node = current_node
                        break
 
                    else:
                        right_node = current_node
                        print(right_node.value, 'right')
                        replace_node = self._find_min_right(current_node)
 
                        if direction == 'left':
                            parent_node.left = replace_node
                            replace_node.right = right_node
                            replace_node.left = left_node
                            break
 
                        else:
                            parent_node.right = replace_node
                            replace_node.right = right_node
                            replace_node.left = left_node
                            break
                    
                
    
    def _leaf(self, node):
        return node.left == None and node.right == None
 
    def _one_child(self, node):
        return node.left == None and isinstance(node.right.value, int) or \
                   isinstance(node.left.value, int) and node.right == None
 
    def _2_children(self, node):
        return isinstance(node.left.value, int) and isinstance(node.right.value, int)
    
    def _have_right_child(self, node):
        try:
            return isinstance(node.right.value, int)
        except:
            return False
    
    def _have_left_child(self, node):
        try:
            return isinstance(node.left.value, int)
 
        except:
            return False
 
    def _find_min_right(self, node):
 
        if self._leaf(node):
            return node
 
        elif self._have_left_child(node):
            prev_node = node
            node = node.left
 
            if self._leaf(node):
                prev_node.left = None
                return node
 
            elif self._have_right_child(node) and not self._have_left_child(node):
                prev_node.left = node.right
                return node
 
            else:
                prev_node = node
                node = node.left
                return self._find_min_right(node)
        
        else:
            return node

bst = BinarySearchTree()
bst.insert(9)    
bst.insert(4)                       
bst.insert(6)                       
bst.insert(20)  
bst.insert(170)
bst.insert(15)
bst.insert(1)           
bst.remove(1)   

print(bst.lookup(1))