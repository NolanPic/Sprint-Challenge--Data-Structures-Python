from collections import deque

class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # what if the value is more than that of the root?
        # what if the value is the same as that of the root?
        if value >= self.value:
            # go right
            if not self.right:
                # there is nothing to the right--add the value here
                self.right = BSTNode(value)
                return
            else:
                return self.right.insert(value)
            
        # what if the value is less than that of the root?
        if value < self.value:
            # go left
            if not self.left:
                # there is nothing to the left--add the value here
                self.left = BSTNode(value)
                return
            else:
                return self.left.insert(value)
        

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True
        if target < self.value:
            # target is smaller--go left
            if self.left is not None:
                # continue the search left
                return self.left.contains(target)
            else:
                # we've reached the end with no matches
                return False
        if target > self.value:
            # target is larger--go right
            if self.right is not None:
                # continue the search right
                return self.right.contains(target)
            else:
                # we've reached the end with no matches
                return False