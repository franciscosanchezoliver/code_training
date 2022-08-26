from typing import Optional
from re import S

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

class Solution:

    def invertTree(
        self, 
        root: Optional[TreeNode]
    ) -> Optional[TreeNode]:

        # Stop condition
        if not root:
            return None

        # Swap the children
        temp = root.left
        root.left = root.right
        root.right = temp

        # Recursive call to each sub trees
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


if __name__=="__main__":
    print("hola")

    nodo4 = TreeNode(4)
    nodo2 = TreeNode(2)
    nodo7 = TreeNode(7)
    nodo1 = TreeNode(1)
    nodo3 = TreeNode(3)
    nodo6 = TreeNode(6)
    nodo9 = TreeNode(9)

    nodo4.left = nodo2
    nodo4.right = nodo7
    
    nodo2.left = nodo1
    nodo2.right = nodo3

    nodo7.left = nodo6
    nodo7.right = nodo9

    solution = Solution()

    result = solution.invertTree(root= nodo4)
    print("end")


