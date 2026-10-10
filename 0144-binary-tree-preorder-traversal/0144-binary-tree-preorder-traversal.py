
class Solution:
    def preorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        ans = []
        ans.append(root.val)
        ans.extend(self.preorderTraversal(root.left))
        ans.extend(self.preorderTraversal(root.right))
        return ans
