
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        results = []
        if root is None:
            return results

        queue = deque([root])

        while queue:
            level = []
            size = len(queue)

            for i in range(size):
                e = queue.popleft()
                level.append(e.val)

                if e.left is not None:
                    queue.append(e.left)

                if e.right is not None:
                    queue.append(e.right)

            results.append(level)

        return results
