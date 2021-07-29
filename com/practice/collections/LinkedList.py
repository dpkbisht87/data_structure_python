class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
        
    def insert_to_head(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
    
    def insert_at_last(self, data):
        new_node = Node(data)
        if self.head:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        else:
            self.head = new_node
            
    def print_linked_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
        
LL = LinkedList()
# LL.insert_to_head(1)
# LL.insert_to_head(2)
# LL.insert_to_head(3)
# LL.insert_to_head(4)
# LL.insert_to_head(5)


LL.insert_at_last(1)
LL.insert_at_last(2)
LL.insert_at_last(3)
LL.insert_at_last(4)
LL.insert_at_last(5)

LL.print_linked_list()