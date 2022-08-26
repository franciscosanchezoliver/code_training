from typing import Optional
from math import inf

class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right

        def __repr__(self) -> str:
            return str(self.val)


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def check_if_valid(root, min, max):
            if not root: # An empty Tree is still a valid BST
                return True

            if not(root.val > min and root.val < max): 
                return False

            return check_if_valid(root.left, min, root.val) and \
                   check_if_valid(root.right, root.val, max)

        res = check_if_valid(root, -inf, inf)

        return res
        

if __name__ == "__main__":
    solution = Solution()

    node2 = TreeNode(2)
    node3 = TreeNode(2)
    node4 = TreeNode(2)
    node2.left = node3
    node2.right = node4
    res = solution.isValidBST(node2)
    assert(res, False)

    node5 = TreeNode(5)
    node4 = TreeNode(4)
    node6 = TreeNode(6)
    node3 = TreeNode(3)
    node7 = TreeNode(7)

    node5.left = node4
    node5.right = node6
    node6.left = node3
    node6.right = node7
    res = solution.isValidBST(node5)
    assert(res, False)


    node5 = TreeNode(5)
    node3 = TreeNode(3)
    node7 = TreeNode(7)
    node4 = TreeNode(4)
    node8 = TreeNode(8)
    
    node5.left = node3
    node5.right = node7
    node7.left = node4
    node7.right = node8

    res = solution.isValidBST(node5)
    assert(res, False)

    node2 = TreeNode(2)
    node1 = TreeNode(1)
    node3 = TreeNode(3)

    node2.left = node1
    node2.right = node3

    res = solution.isValidBST(node2)
    assert(res, True)

    node2 = TreeNode(2)
    node2.left = TreeNode(2)
    node2.right = TreeNode(3)

    res = solution.isValidBST(node2)
    assert(res, False)