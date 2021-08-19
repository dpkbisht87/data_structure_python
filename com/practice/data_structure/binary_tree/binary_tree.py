class Queue(object):
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1].value

    def __len__(self):
        return self.size()

    def size(self):
        return len(self.items)

class Stack(object):
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def __str__(self):
        s = ""
        for i in range(len(self.items)):
            s += str(self.items[i].value) + "-"
        return s

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def print_tree(self, traversal_type):
        if traversal_type == 'preorder':
            return self.preorder_print(tree.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(tree.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(tree.root, "")

    def preorder_print(self, node, traversal):
        if node:
            traversal += (str(node.value) + "-")
            traversal = self.preorder_print(node.left, traversal)
            traversal = self.preorder_print(node.right, traversal)
        return traversal

    def inorder_print(self, node, traversal):
        if node:
            traversal = self.inorder_print(node.left, traversal)
            traversal += (str(node.value) + "-")
            traversal = self.inorder_print(node.right, traversal)
        return traversal

    def postorder_print(self, node, traversal):
        if node:
            traversal = self.postorder_print(node.left, traversal)
            traversal = self.postorder_print(node.right, traversal)
            traversal += (str(node.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)

        traversal = ""
        while not queue.is_empty():
            cur = queue.dequeue()
            traversal += str(cur.value) + "-"

            if cur.left:
                queue.enqueue(cur.left)
            if cur.right:
                queue.enqueue(cur.right)
        return traversal

    def reverse_levelorder_print(self, start):
        if start is None:
            return
        q = Queue()
        s = Stack()
        q.enqueue(start)

        traversal = ""
        while not q.is_empty():
            cur = q.dequeue()
            s.push(cur.value)

            if cur.right:
                q.enqueue(cur.right)

            if cur.left:
                q.enqueue(cur.left)

        while not s.is_empty():
            traversal += str(s.pop()) + "-"
        return traversal

    def height(self, node):
        if node is None:
            return -1
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        return 1 + max(left_height, right_height)

tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# print(tree.print_tree("preorder"))
# print(tree.print_tree("inorder"))
# print(tree.print_tree("postorder"))

# print(tree.levelorder_print(tree.root))
# print(tree.reverse_levelorder_print(tree.root))
print(tree.height(tree.root))