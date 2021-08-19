class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        return self.insert_helper(self.root, new_val)

    def  insert_helper(self, node, new_val):
        if node.data > new_val:
            if node.left:
                self.insert_helper(node.left, new_val)
            else:
                node.left = Node(new_val)
        else:
            if node.right:
                self.insert_helper(node.right, new_val)
            else:
                node.right = Node(new_val)

    def search(self, find_val):
        return self.search_helper(self.root, find_val)

    def search_helper(self, node, find_val):
        if node:
            if node.data == find_val:
                return True
            elif node.data > find_val:
                return self.search_helper(node.left, find_val)
            else:
                return self.search_helper(node.right, find_val)
        else:
            return False

bst = BST(10)
bst.insert(3)
bst.insert(1)
bst.insert(25)
bst.insert(9)
bst.insert(13)

print(bst.search(9))
print(bst.search(14))