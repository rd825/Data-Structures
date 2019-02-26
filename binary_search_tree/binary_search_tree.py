class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        # if inserted val < current node val, go left
        if value <= self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                # call insert on left child
                self.left.insert(value)
        else:  # go right
            if self.right is None:
                self.right = BinarySearchTree(value)  # insert node
            else:
                # call insert on right child
                self.right.insert(value)

    def contains(self, target):
        # search BST for given value returning boolean
        if target == self.value:  # it exists
            return True
        elif target < self.value:  # go left
            if self.left is None:
                return False
            else:
                return self.left.contains(target)  # recurse
        else:
            if self.right is None:  # go right
                return False
            else:
                return self.right.contains(target)  # recurse

    def get_max(self):
        currentNode = self
        while currentNode.right:
            currentNode = currentNode.right
        return currentNode.value
