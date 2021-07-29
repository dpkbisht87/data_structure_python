class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None


    def insertToHead(self, data):
        new_node = Node(data);
        if self.head:
            new_node. next = self.head
            self.head = new_node
        else:
            self.head = new_node

    def insertToTail(self, data):
        new_node = Node(data)
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
        else:
            self.head = new_node

    def printList(self):
        cur = self.head
        while cur:
            print(cur.data)
            cur = cur.next

    def hasLoop(self):
        if not self.head:
            return False
        slowP, fastP = self.head, self.head
            

LL = LinkedList()
LL.insertToHead(1)
LL.insertToHead(2)
LL.insertToHead(3)
LL.insertToHead(4)
LL.insertToHead(5)

LL.head.next.next.next = LL.head.next

# LL.insertToTail(1)
# LL.insertToTail(2)
# LL.insertToTail(3)
# LL.insertToTail(4)
# LL.insertToTail(5)

LL.printList()