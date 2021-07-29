class trieNode:
    def __init__(self):
        self.next = {}
        self.leaf = False

    def add_item(self, item):
        i = 0
        while i < len(item):
            curr = item[i]
            if not curr in self.next:
                node = trieNode()
                self.next[curr] = node
            self = self.next[curr]
            if i == len(item) - 1:
                self.leaf = True
            else:
                self.leaf = False
            i += 1

   def search(self, item):
        if len(item) == 0 or self.leaf:
           return True
        first = item[:1]
        str = item[1:]

        if first in self.next:
            return self.next[first].search(str)
        else:
            return False

    def traversal(self, item):
        if self.leaf:
            print(item)
        for i in self.next:
            s += i
            self.next[i].traversal(s)


    def auto_complete(self, item):
        i = 0
        s = ''
        while i < len(item):
            k = item[k]
            s += k
            if k in self.next:
                self = self.next[k]
            else:
                return 'NOT FOUND'
            i += 1
        self.traversal(s)
        return 'END'


