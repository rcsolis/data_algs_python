# BINARY SEARCH TREES

class BST:
    def __init__(self, data, left = None, right = None) -> None:
        self.data = data
        self.left = left
        self.right = right

    def insert(self, data):
        if self.data == data:
            return False # Duplicate value
        
        if data < self.data:
            if self.left is None:
                self.left = BST(data)
                return True
            else: # If has child
                return self.left.insert(data)
        else:
            if self.right is None:
                self.right = BST(data)
                return True
            else: # If has child
                return self.right.insert(data)

    def find(self, data):
        # end condition, if data found
        if self.data == data:
            return True
        # if data is less than current data
        if data < self.data:
            # If its a leaf
            if self.left is None:
                return False
            else: # search in left side
                return self.left.find(data)
        else: # if data is greater than current data
            if self.righ is None: # if its a leaf
                return False
            else: # search in the right side
                return self.right.find(data)
    
    def get_size(self):
        # Formula 1 + size(left) + size(right)
        # If its a leaf    
        if self.left is None and self.right is None:
            return 1
        else:
            # if has both
            if self.left is not None and self.right is not None:
                return 1 + self.left.get_size() + self.right.get_size()
            else:
                # if has left
                if self.left is not None:
                    return 1 + self.left.get_size()
                # if has right
                if self.right is not None:
                    return 1 + self.right.get_size()

    def preorder(self):
        print(f"({self.data})")
        # if is a leaf
        if self.left is None and self.right is None:
            return
        else:
            if self.left is not None:
                self.left.preorder()
            if self.right is not None:
                self.right.preorder()

    def inorder(self):
        # if is a leaf
        if self.left is None and self.right is None:
            print(f"({self.data})")
            return
        if self.left is not None:
            self.left.inorder()
        print(f"({self.data})")
        if self.right is not None:
            self.right.inorder()

    def delete(self):
        pass

# TEST Binary Search Tree
print("Binary Search Tree")

bst = BST(5)
bst.insert(3)
bst.insert(8)
bst.insert(1)
bst.insert(4)
bst.insert(6)
bst.insert(9)
print("CURRENT SIZE:")
print(bst.get_size())
print("PREORDER:")
bst.preorder()
print("INORDER:")
bst.inorder()
