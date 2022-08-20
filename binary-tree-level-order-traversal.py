from doctest import OutputChecker
from typing import Optional, List
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque()
        q.append(root)
        while q:
            lvl = []
            n = len(q)
            for i in range(n):
                node = q.popleft()
                if node:
                    lvl.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
                
            if lvl:
                res.append(lvl)
        return res



if __name__ == "__main__":
    solution = Solution()

    node3 = TreeNode(3)
    node9 = TreeNode(9)
    node20 = TreeNode(20)
    node15 = TreeNode(15)
    node7 = TreeNode(7)

    node3.left = node9
    node3.right = node20

    node20.left = node15
    node20.right = node7

    res = solution.levelOrder(node3)
    print(res)
    assert (res, [[3], [9, 20], [15, 7]])
