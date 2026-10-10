
class Solution:
    def postorder(self, root: 'Node') -> list[int]:
        if root is None:
            return []

        ans = []
        for child in root.children:
            ans.extend(self.postorder(child))

        ans.append(root.val)
        return ans
