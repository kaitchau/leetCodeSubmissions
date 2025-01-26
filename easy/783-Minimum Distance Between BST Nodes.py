# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    node_values = []
    def preorder(self, root):
        if root is None:
            return null
        node_values.append(root.val)
        self.preorder(root.left)
        self.preorder(root.right)

    def minDiffInBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        min_diff = 9999
        self.preorder(root)
        skip=0
        for i in range(len(node_values)):
            for j in range(i,len(node_values)):
                if max(node_values[i],node_values[j]) - min(node_values[i],node_values[j]) < min:
                    min_diff = max(node_values[i],node_values[j]) - min(node_values[i],node_values[j])

            

        