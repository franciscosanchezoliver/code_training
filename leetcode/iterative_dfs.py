
from reprlib import recursive_repr


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

    def recursive_inorder(
        self, 
        root: TreeNode, 
    ):
        if not root:
            return None
        self.recursive_inorder(root.left)
        print(root.val, end=" ")
        self.recursive_inorder(root.right)
        

    def iterative_preorder(
        self, 
        root: TreeNode,
        stack = []
    ): 
        stack.append(root)

        while len(stack) > 0:
            next = stack.pop()
            if next is not None:
                print(next.val, end=" ")
                stack.append(next.right)
                stack.append(next.left)

    def iterative_inorder(
        self, 
        root: TreeNode,
        stack = []
    ):
        stack.append(root)

        while len(stack) > 0:
            next = stack.pop()
            if next is not None:
                stack.append(next.right)
                stack.append(next.left)
                print(next.val, end=" ")



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
    walker.iterative_inorder(nodo15)
    #walker.recursive_inorder(nodo15)