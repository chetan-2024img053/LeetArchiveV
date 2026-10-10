
class Solution:
    def postorderTraversal(self, root: TreeNode | None) -> list[int]:
        if root is None:
            return []

        ans = []
        ans.extend(self.postorderTraversal(root.left))
        ans.extend(self.postorderTraversal(root.right))
        ans.append(root.val)

        return ans
