    # Define variables for traversing tree
        parent = None
        current = self.root
    
        # Find the node to delete 
        while current and key != current.value: 
            parent = current
            current = current.left if key < current.value else current.right
    
        # If we found a match, check the three cases
        if current != None:
    
            # Case 1: No children
            if not (current.left or current.right): 
                if parent == None: 
                    self.root = None 
                else: 
                    if current == parent.left: 
                        parent.left = None 
                    else: 
                        parent.right = None
    
            # Case 2: Only one child
            elif not(current.left and current.right): 
                child = current.left if current.left else current.right 
                if parent == None: 
                    self.root = child 
                else: 
                    if current == parent.left:
                        parent.left = child 
                    else: 
                        parent.right = child
    
            # Case 3: Two children
            else: 
                # Find successor and its parent 
                successor_parent = current 
                successor_node = current.right 
                while successor_node.left: 
                    successor_parent = successor_node 
                    successor_node = successor_node.left
    
                # Delete successor
                successor_parent.left = successor_node.right
    
                # Replace current node with value of successor 
                current.value = successor_node.value
    
                # Relink the root node if necessary
                if not current.parent: 
                    self.root = current