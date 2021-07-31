class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new_node

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            return
        new_node = Node(data)

        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev_node = None
        while cur_node and cur_node != key:
            prev_node = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev_node.next = cur_node.next
        cur_node = None

    def del_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None

            prev_node = None
            index = 0
            while cur_node or index != pos:
                prev = cur_node
                cur_node = cur_node.next

            if cur_node is None:
                return
            prev_node.next = cur_node.next
            cur_node = None



llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")

llist.prepend("D")

llist.print_list()