from math import radians
from typing import Optional
from re import T


class TreeNode:

    def __init__(
        self, 
        val=0,
        left=None,
        right=None
    ):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)

class Walk:

    def preorder_recursive(
        self, 
        root: Optional[TreeNode]
    ):
        # R I Z
        if not root:
            return None

        print (root.val)
        self.preorder_recursive(root.left)
        self.preorder_recursive(root.right)

    def inorder_recursive(
        self, 
        root: Optional[TreeNode]
    ):
        # I R D
        if not root:
            return None

        self.inorder_recursive(root.left) 
        print(root.val)
        self.inorder_recursive(root.right)

    def postorder_recursive(
        self,
        root: Optional[TreeNode]
    ):
        # I D R
        if not root:
            return None
        
        self.postorder_recursive(root.left)
        self.postorder_recursive(root.right)
        print(root.val)

    def iterative_preorder(
        self, 
        root: Optional[TreeNode],
        stack = []
    ): 
        # R I D
        stack.append(root)

        while len(stack) > 0:
            node = stack.pop()
            if node is not None:
                print(node.val)
                stack.append(node.right)
                stack.append(node.left)

    #def iterative_inorder(
    #    self, 
    #    root: Optional[TreeNode],
    #    stack = []
    #):
    #    stack.append(root)

    #    while len(stack) > 0:
    #        node = stack.pop()

    #        if node is not None:
    #            stack.append(node.right)
    #            print(node.val)
    #            stack.append(node.left)


# Recursive 
def walk(tree):
    if tree is not None:
        print(tree)
        walk(tree.left)
        walk(tree.right)


if __name__ == "__main__":
    print("hello")
    nodo15 = TreeNode(15)
    nodo9 = TreeNode(9)
    nodo6 = TreeNode(6)
    nodo14 = TreeNode(14)
    nodo13 = TreeNode(13)
    nodo20 = TreeNode(20)
    nodo17 = TreeNode(17)
    nodo64 = TreeNode(64)
    nodo26 = TreeNode(26)
    nodo72 = TreeNode(72)

    nodo15.left = nodo9
    nodo15.right = nodo20

    nodo9.left = nodo6
    nodo9.right = nodo14

    nodo14.left = nodo13

    nodo20.left = nodo17
    nodo20.right= nodo64

    nodo64.left = nodo26
    nodo64.right = nodo72

    walker = Walk()
    #print("Preorder Recursive")
    #walker.preorder_recursive(nodo15)
    
    #print("Inorder Recursive")
    walker.inorder_recursive(nodo15)

    #print("Postorder Recursive")
    #walker.postorder_recursive(nodo15)
    #print("end")

    #walker.iterative_preorder(nodo15)
    #walker.iterative_inorder(nodo15)

