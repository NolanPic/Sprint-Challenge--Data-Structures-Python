class Node:
    def __init__(self, value=None, next_node=None):
        self.value = value
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        self.next_node = new_next
        
    def __str__(self):
        return f'{self.value}'

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, value):
        node = Node(value)

        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False

        current = self.head

        while current:
            if current.get_value() == value:
                return True

            current = current.get_next()

        return False
    
    def __str__(self):
        current = self.head
        while current:
            print(f'{current} --> {current.next_node}')
            current = current.get_next()

    # 1 -> 2 -> 3 -> 4 -> None
    # 4 -> 3 -> 2 -> 1 -> None
    # None <- 1 <- 2 <- 3 <- 4
    def reverse_list(self, node, prev):
        # base case
        if(node == None):
            self.head = prev
            return
        # recursive case
        next_node = node.get_next()
        node.next_node = prev
        prev = node
        node = next_node
        
        self.reverse_list(node, prev)
        
        
