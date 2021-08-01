from typing import Counter


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self) -> None:
        self.head = None

    def prepend(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        new_node.next = self.head
        self.head = new_node
        cur.next = new_node

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            cur.next = new_node
            new_node.next = self.head

    def print_list(self):
        cur = self.head
        while cur:
            print(cur.data, end = ' ')
            cur = cur.next
            if cur == self.head:
                break
        print()

    def remove(self, key):
        if not self.head:
            return
        else:
            if self.head.data == key:
                cur = self.head
                while cur.next != self.head:
                    cur = cur.next
                if self.head == self.head.next:
                    self.head = None
                else:
                    cur.next = self.head.next
                    self.head = self.head.next
            else:
                prev = None
                cur = self.head
                while cur.next != self.head:
                    prev = cur
                    cur = cur.next
                    if cur.data == key:
                        prev.next = cur.next
                        cur = cur.next

    def __len__(self):
        cur = self.head
        count = 0
        while cur.next:
            count += 1
            cur = cur.next
            if cur == self.head:
                break
        return count

    def split_list(self):
        size =len(self)
        if size == 0:
            return None
        if size == 1:
            return self.head

        mid = size // 2
        count = 0
        prev = None
        cur = self.head
        while cur and count < mid:
            prev = cur
            cur = cur.next
            count += 1
        prev.next = self.head
        split_list = CircularLinkedList()
        while cur.next != self.head:
            split_list.append(cur.data)
            cur = cur.next
        split_list.append(cur.data)

        self.print_list()
        print("\n")
        split_list.print_list()

    def remove_node(self, node):
        if self.head == node:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
        else:
            cur = self.head
            prev = None
            while cur.next != self.head:
                prev = cur
                cur = cur.next
                if cur == node:
                   prev.next = cur.next
                   cur = cur.next

    def josephus_circle(self, step):
        cur = self.head

        length = len(self)
        while length > 1:
            count = 1
            while count != step:
                cur = cur.next
                count += 1
            print("KILL:" + str(cur.data))
            self.remove_node(cur)
            cur = cur.next
            length -= 1

llist = CircularLinkedList()
llist.append('A')
llist.append('B')
llist.append('C')
llist.append('D')
llist.append('E')
llist.append('F')

# llist.print_list()
llist.split_list()
