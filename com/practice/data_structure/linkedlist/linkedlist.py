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
            print(cur_node.data, end=' ')
            cur_node = cur_node.next
        print()

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insert_after_node(self, prev, data):
        if not prev:
            return
        new_node = Node(data)

        new_node.next = prev.next
        prev.next = new_node

    def delete_node(self, key):
        cur_node = self.head
        if cur_node and cur_node.data == key:
            self.head = cur_node.next
            cur_node = None
            return

        prev = None
        while cur_node and cur_node.data != key:
            prev = cur_node
            cur_node = cur_node.next

        if cur_node is None:
            return
        prev.next = cur_node.next
        cur_node = None

    def delete_node_at_pos(self, pos):
        if self.head:
            cur_node = self.head
            if pos == 0:
                self.head = cur_node.next
                cur_node = None

            prev = None
            index = 0
            while cur_node and index != pos:
                prev = cur_node
                cur_node = cur_node.next
                index += 1

            if cur_node is None:
                return

            prev.next = cur_node.next
            cur_node = None

    def len_iterative(self):
        len = 0
        cur = self.head
        while cur:
            cur = cur.next
            len += 1
        return len

    def len_recursive(self, node):
        if node is None:
            return 0
        return 1 + self.len_recursive(node.next)

    def swap_nodes(self, key_1, key_2):
        if key_1 == key_2:
            return

        cur_1 = self.head
        prev_1 = None
        while cur_1 and cur_1.data != key_1:
            prev_1 = cur_1
            cur_1 = cur_1.next

        cur_2 = self.head
        prev_2 = None
        while cur_2 and cur_2.data != key_2:
            prev_2 = cur_2
            cur_2 = cur_2.next

        if not cur_1 or not cur_2:
            return

        if prev_1:
            prev_1.next = cur_2
        else:
            self.head = cur_2

        if prev_2:
            prev_2.next = cur_1
        else:
            self.head = cur_2
        cur_2.next, cur_1.next = cur_1.next, cur_2.next

    def reverse_iterative(self):
        prev = None
        cur = self.head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        self.head = prev

    def reverse_recursive(self):
        def _reverse_recursive(cur, prev):
            if cur is None:
                return prev
            nxt = cur.next
            cur.next = prev
            cur = nxt
            return _reverse_recursive(cur, prev)

        self.head = _reverse_recursive(cur=self.head, prev=None)

    def merge_sorted(self, llist):
        p = self.head
        q = llist.head
        s = None
        if not p:
            return q
        if not q:
            return p

        if p and q:
            if p.data <= q.data:
                s = p
                p = s.next
            else:
                s = q
                q = s.next
            new_head = s

        while p and q:
            if p.data <= q.data:
                s.next = p
                s = p
                p = s.next
            else:
                s.next = q
                s = q
                q = s.next

        if not p:
            s.next = q
        if not q:
            s.next = p
        self.head = new_head
        return self.head

    def remove_duplicates(self):
        temp_dict = {}
        cur = self.head
        prev = None

        while cur:
            print(cur.data, temp_dict)
            if cur.data in temp_dict.keys():
                # Is duplicate. Remove the node
                prev.next = cur.next
                cur = None
            else:
                temp_dict[cur.data] = 1
                prev = cur
            cur = prev.next

    # This approach takes two loops
    def print_nth_from_last(self, n):
        # find Length
        list_len = 0
        cur = self.head
        while cur:
            list_len += 1
            cur = cur.next
        cur = self.head
        while cur and list_len != n:
            cur = cur.next
            list_len -= 1
        return cur.data

    def print_nth_from_last_in_single_iteration(self, n):
        start = self.head
        end  = self.head
        cur = self.head
        index = 0
        while end:
            if index < n:
                index += 1
            else:
                start = start.next
            end = end.next

        return start.data

    def count_occurences_iterative(self, data):
        cur = self.head
        count = 0
        while cur:
            if cur.data == data:
                count += 1
            cur = cur.next
        return count

    def count_occurrences_recursive(self, data):
        node = self.head
        def _recursive_helper(node, data):
            if not node:
                return 0
            if node.data == data:
                return 1 + _recursive_helper(node.next, data)
            else:
                return _recursive_helper(node.next, data)
        return _recursive_helper(node, data)

    def rotate(self, k):
        cur = self.head
        last_node = None
        pivot_node = None
        while cur:
            if cur.data == k:
                pivot_node = cur
            if cur.next is None:
                last_node = cur
            cur = cur.next

        last_node.next = self.head
        self.head = pivot_node.next
        pivot_node.next = None

    def is_pallindrom_sting_method(self):
        cur = self.head
        s = ''
        while cur:
            s += cur.data
            cur = cur.next
        return s == s[::-1]

    def is_pallindrom_using_stack(self):
        s = []
        lst = []
        cur = self.head
        while cur:
            lst.append(cur.data)
            s.append(cur.data)
            cur = cur.next

        index = 0
        while s:
            if s.pop() == lst[index]:
                index += 1
            else:
                return False
        return True

    def is_pallindrom_using_two_pointers(self):
        if self.head:
            first_p = self.head
            last_p = self.head
            value_list = []
            len_list = 0
            while last_p:
                value_list.append(last_p.data)
                len_list += 1
                last_p = last_p.next

            for i in range(1, (len_list // 2) + 1):
                if first_p.data != value_list[-i]:
                    return False
                first_p = first_p.next
            return True
        else:
            return True

# IS PALLINDROME
llist_2 = LinkedList()
llist_2.append("R")
llist_2.append("A")
llist_2.append("D")
llist_2.append("A")
llist_2.append("R")

# print(llist_2.is_pallindrom_using_sting())
print(llist_2.is_pallindrom_using_stack())
print(llist_2.is_pallindrom_using_two_pointers())

#ROTATE AROUND A NODE
# llist = LinkedList()
# llist.append(1)
# llist.append(2)
# llist.append(3)
# llist.append(4)
# llist.append(5)
# llist.append(6)

# llist.rotate(5)
# llist.print_list()

# COUNT OCCURRNCES
# llist_2 = LinkedList()
# llist_2.append(1)
# llist_2.append(2)
# llist_2.append(1)
# llist_2.append(3)
# llist_2.append(1)
# llist_2.append(4)
# llist_2.append(1)
# print(llist_2.count_occurences_iterative(1))
# print(llist_2.count_occurrences_recursive(1))

# Remove duplicates
# llist = LinkedList()
# llist.append(1)
# llist.append(6)
# llist.append(1)
# llist.append(4)
# llist.append(2)
# llist.append(2)
# llist.append(4)

# print("Original Linked List")
# llist.print_list()
# print("Linked List After Removing Duplicates")
# llist.remove_duplicates()
# llist.print_list()

# llist = LinkedList()
# llist.append("A")
# llist.append("B")
# llist.append("C")
# llist.append("D")
# llist.append("E")
# llist.append("F")

# llist.print_list()
# llist.prepend("F")
# llist.delete_node_at_pos(1)
# llist.delete_node("B")
# print(llist.len_iterative())
# print(llist.len_recursive(llist.head))
# llist.swap_nodes('F', 'F')
# llist.reverse_iterative()
# print('------------')
# llist.print_list()

# print(llist.print_nth_from_last(2))
# print(llist.print_nth_from_last_in_single_iteration(2))

# Merge Sorted list
# llist_1 = LinkedList()
# llist_2 = LinkedList()

# llist_1.append(1)
# llist_1.append(5)
# llist_1.append(7)
# llist_1.append(9)
# llist_1.append(10)

# llist_2.append(2)
# llist_2.append(3)
# llist_2.append(4)
# llist_2.append(6)
# llist_2.append(8)

# llist_1.merge_sorted(llist_2)
# llist_1.print_list()




