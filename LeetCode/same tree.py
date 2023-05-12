## check whether the given two trees are same or not

class Node:
    def __init__(self, data):
        self.right = None
        self.data = data
        self.left = None


class BST:
    def createRoot(self, value):
        self.root = Node(value)
        return self.root

    def insert(self, value):
        node = Node(value)
        if self.root is None:
            return node

        curr = self.root
        while True:
            if value < curr.data:
                if curr.left == None:
                    curr.left = node
                    break
                curr = curr.left
            else:
                if curr.right == None:
                    curr.right = node
                    break
                curr = curr.right
        return self.root

    def areSame(self, n1, n2):
        if not n1 and not n2:
            return True

        if not n1 or not n2:
            return False

        if n1.data != n2.data:
            return False
        return self.areSame(n1.left, n2.left) and self.areSame(n1.right, n2.right)


n1 = BST()
n1.createRoot(3)
n1.insert(2)
n1.insert(1)

n2 = BST()
n2.createRoot(3)
n2.insert(2)
n2.insert(1)

print(n1.areSame(n1.root, n2.root))
