"""
Operations of BST:
Insertion
Searching
Deletion

Auxiliary operations
Find the height of tree
Find number of levels in BST
Find the maximum value in the BST
"""
from collections import defaultdict

class Node(object):
    def __init__(self, val):
        self.l_child = None
        self.r_child = None
        self.val = val


class BinarySearchTree(object):

    """Basic Operations"""

    def insert(self, root, node):
        if root is None:
            return node
        if root.val < node.val:
            root.r_child = self.insert(root.r_child, node)
        else:
            root.l_child = self.insert(root.l_child, node)
        return root

    def search(self, root, key):
        if root is None:
            return "Data Not Found or Tree is empty"
        if root.val == key:
            return "Found it"
        elif root.val < key:
            return self.search(root.r_child, key)
        elif root.val > key:
            return self.search(root.l_child, key)

    """BST Traversals"""

    def in_order_place(self, root):
        if not root:
            return None
        else:
            self.in_order_place(root.l_child)
            print(root.val, end=" ")
            self.in_order_place(root.r_child)

    def pre_order_place(self, root):
        if not root:
            return None
        else:
            print(root.val)
            self.pre_order_place(root.l_child)
            self.pre_order_place(root.r_child)

    def post_order_place(self, root):
        if not root:
            return None
        else:
            self.post_order_place(root.l_child)
            self.post_order_place(root.r_child)
            print(root.val)
    '''Our goal is to find all the Modes in a tree
    A mode is a value that has the maximum frequency
    Approach is use a Hashmap using DFS or tree traversal technique
    '''
    def ModeofBST(self, root):
        # using inorder traversal traverse all the nodes and store the counter in hashmap
        def in_order_place(root):
            if not root:
                return None
            else:
                in_order_place(root.l_child)
                # print(root.val, end=" ")
                data[root.val] += 1
                in_order_place(root.r_child)
        
        # defaultdict used for cleaner code
        data = defaultdict(int)
        in_order_place(root)
        l = []
        # finding max frequency value
        maxFreq = max(data.values())

        # finding all the values with same frequency
        for i in data:
            if maxFreq == data[i]:
                l.append(i)
        print(l)
""" Create different node and insert data into it"""
r = Node(0)  # creating root node with choosing 3 as root node value
node = BinarySearchTree()

nodeList = [2]
for nd in nodeList:
    if nd is not None:
        node.insert(r, Node(nd))

node.ModeofBST(r)