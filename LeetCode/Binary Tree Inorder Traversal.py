# create Tree then run the program

class Solution:
    def Inorder(self,root, add):
        if root!=None:
            self.Inorder(root.left, add)
            add.append(root.val)
            self.Inorder(root.right, add)


    def inorderTraversal(self, root):
        add = []
        self.Inorder(root, add)
        return add
