# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        https://leetcode-cn.com/problems/smallest-subtree-with-all-the-deepest-nodes/
        :type root: TreeNode
        :rtype: TreeNode
        给定一个根为root的二叉树，每个节点的深度是 该节点到根的最短距离 。
        如果一个节点在 整个树 的任意节点之间具有最大的深度，则该节点是 最深的 。
        一个节点的 子树 是该节点加上它的所有后代的集合。
        返回能满足 以该节点为根的子树中包含所有最深的节点 这一条件的具有最大深度的节点。
        """

        if not root: return root

        depth = {None: -1}

        def dfs(node, parentNode):
            if node:
                depth[node] = depth[parentNode] + 1
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root, None)

        maxDepth = max(depth.values())

        def answer(node):
            if not node or depth.get(node, None) == maxDepth:
                return node
            left, right = answer(node.left), answer(node.right)
            return node if left and right else left or right

        return answer(root)
