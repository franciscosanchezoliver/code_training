class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return str(self.val)


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        cur = root  
        while cur:
            if p.val < cur.val and q.val < cur.val:
                cur = cur.left
            elif p.val > cur.val and q.val > cur.val:
                cur = cur.right
            else:
                return cur


if __name__ == "__main__":
    solution = Solution()

    node6 = TreeNode(6)
    node2 = TreeNode(2)
    node8 = TreeNode(8)
    node0 = TreeNode(0)
    node4 = TreeNode(4)
    node7 = TreeNode(7)
    node9 = TreeNode(9)
    node3 = TreeNode(3)
    node5 = TreeNode(5)

    node6.left = node2
    node6.right = node8
    node2.left = node0
    node2.right = node4
    node8.left = node7
    node8.right = node9
    node4.left = node3
    node4.right = node5

    #p = 2; q = 8
    #res = solution.lowestCommonAncestor(node6, p, q)
    # print(res)
    #assert(res, 6)

    p = 2
    q = 4
    res = solution.lowestCommonAncestor(node6, p, q)
    print(res)
    assert (res, 2)
