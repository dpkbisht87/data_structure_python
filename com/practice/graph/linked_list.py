from node import Node

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def get_head(self):
        return self.head

    def is_empty(self):
        return self.head is None

    def insert_at_head(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_at_tail(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur:
                cur = cur.next
            cur.next = new_node

    def length(self):
        cur = self.head
        length = 0
        while cur:
            length += 1
            cur = cur.next
        return length

    def print_list(self):
        if self.head is None:
            print('List is empty')
            return False
        cur = self.head
        while cur.next:
            print(cur.data, end = '->')
            cur = cur.next
        print(cur.data, end = '-> None')
        return True

    def delete_at_head(self):
        first = self.head
        if self.head is not None:
            self.head = first.next
            first.next = None
        return

    def delete(self, value):
        deleted = False
        if self.head is None:
            return deleted
        cur = self.head
        prev = None

        if cur.data == value:
            self.head = cur.next
            cur.next = None
            deleted = True
            return deleted

        prev = cur
        cur = cur.next

        while cur:
            if cur.data == value:
                prev.next = cur.next
                cur.next = None
                deleted = True
                break
            prev = cur
            cur = cur.next
        return deleted

    def search(self, data):
        found = False
        if self.head is None:
            return found
        cur = self.head
        while cur:
            if cur.data == data:
                found = True
                break
            cur = cur.next
        return found

    def remove_duplicates(self):
        if self.is_empty():
            return

        # If list only has one node, leave it unchanged
        if self.get_head().next_element is None:
            return

        outer_node = self.get_head()
        while outer_node:
            inner_node = outer_node  # Iterator for the inner loop
            while inner_node:
                if inner_node.next_element:
                    if outer_node.data == inner_node.next_element.data:
                        # Duplicate found, so now removing it
                        new_next_element = inner_node.next_element.next_element
                        inner_node.next_element = new_next_element
                    else:
                        # Otherwise simply iterate ahead
                        inner_node = inner_node.next_element
                else:
                    # Otherwise simply iterate ahead
                    inner_node = inner_node.next_element
            outer_node = outer_node.next_element
        return