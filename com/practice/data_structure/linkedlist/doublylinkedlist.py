class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self) -> None:
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            self.head.prev = new_node
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node
            new_node.prev = cur

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end=' ')
            cur = cur.next
        print()

    def add_after_node(self, key, data):
        cur = self.head
        new_node = Node(data)
        while cur:
            if cur.data == key:
                break
            cur = cur.next
        if cur.next is None:
            self.append(data)
            return
        else:
            new_node.next = cur.next
            cur.next.prev = new_node
            new_node.prev = cur
            cur.next = new_node

    def add_node_before(self, key, data):
        if self.head.data == key:
            self.prepend(data)
        else:
            new_node = Node(data)
            cur = self.head
            prev = None
            while cur:
                if cur.data == key:
                    break
                prev = cur
                cur = cur.next
            prev.next = new_node
            new_node.prev = prev
            new_node.next = cur
            cur.prev = new_node

    def delete(self, key):
        cur = self.head
        while cur:
            if cur.data == key and self.head == cur and cur.next is None:
                self.head = None
                cur = None
            else:
                if self.head.data == key:
                    nxt = cur.next
                    nxt.prev = None
                    self.head = nxt
                    cur = None
                else:
                    prev = None
                    while cur:
                        if cur.data == key:
                            break
                        prev = cur
                        cur = cur.next
                    if cur.next:
                        nxt = cur.next
                        prev.next = nxt
                        nxt.prev = prev
                        cur = None
                    else:
                        prev.next = None
                        cur = None

    def reverse(self):
        tmp = None
        cur = self.head
        while cur:
            tmp = cur.prev
            cur.prev = cur.next
            cur.next = tmp
            cur = cur.prev
        if tmp:
            self.head = tmp.prev


llist = DoublyLinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')
llist.append('F')

llist.print_list()
# llist.add_after_node('F', 'K')
# llist.add_node_before('A', 'K')
# llist.delete('F')
llist.reverse()
llist.print_list()

