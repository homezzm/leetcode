# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def lcaDeepestLeaves(self, root):
        """
        https://leetcode-cn.com/problems/lowest-common-ancestor-of-deepest-leaves/
        :type root: TreeNode
        :rtype: TreeNode
        给你一个有根节点的二叉树，找到它最深的叶节点的最近公共祖先。
        回想一下：
        叶节点 是二叉树中没有子节点的节点
        树的根节点的深度为0，如果某一节点的深度为d，那它的子节点的深度就是d+1
        如果我们假定 A 是一组节点S的 最近公共祖先，S中的每个节点都在以 A 为根节点的子树中，且 A的深度达到此条件下可能的最大值。
        """
        if not root: return root

        # 先找标记每个节点的深度
        depth = {None: -1}

        def dfs(node, parentNode):
            if not node: return
            depth[node] = depth[parentNode] + 1
            dfs(node.left, node)
            dfs(node.right, node)

        dfs(root, None)

        maxDepth = max(depth.values())

        def answer(node):
            #如果是空，或当前节点就是最深的节点，就将它返回
            if not node or depth.get(node, None) == maxDepth:
                return node
            left, right = answer(node.left), answer(node.right)

            return node if left and right else left or right

        return answer(root)
