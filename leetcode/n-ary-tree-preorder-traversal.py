from collections import deque
from typing import List

class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

    def __repr__(self) -> str:
        return str(self.val)

class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        output = []

        def dfs(node):
            if not node: return 

            output.append(node.val)

            if node.children:
                for child in node.children:
                    dfs(child)

        dfs(root)

        return output

    def preorder_iterative(self, root: 'Node') -> List[int]:

        if not root:  return []
        
        q = deque([root])
        output = []

        while q: 
            cand = q.popleft()
            output.append(cand.val)

            for c in reversed(cand.children):
                q.appendleft(c)

        return output




if __name__ == "__main__":
    solution = Solution()

    nodo1 = Node(val= 1)
    nodo3 = Node(val= 3)
    nodo2 = Node(val= 2)
    nodo4 = Node(val= 4)
    nodo5 = Node(val= 5)
    nodo6 = Node(val= 6)

    nodo1.children = [nodo3, nodo2, nodo4]
    nodo3.children = [nodo5, nodo6]

    res = solution.preorder_iterative(nodo1)
    print(res)
    

        