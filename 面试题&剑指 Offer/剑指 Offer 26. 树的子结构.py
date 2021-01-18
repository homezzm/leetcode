# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSubStructure(self, A, B):
        """
        https://leetcode-cn.com/problems/shu-de-zi-jie-gou-lcof/
        :type A: TreeNode
        :type B: TreeNode
        :rtype: bool
        输入两棵二叉树A和B，判断B是不是A的子结构。(约定空树不是任意一个树的子结构)
        B是A的子结构， 即 A中有出现和B相同的结构和节点值。
        """
        if not A or not B: return False

        def dfs(nodeA, nodeB):
            if not nodeB: return True
            if not nodeA: return False
            # 如果 A 的当前节点值与 B 的根节点值相同，我们调用 dfs 函数判断子树是否也相同；
            return nodeA.val == nodeB.val and \
                   dfs(nodeA.left, nodeB.left) and \
                   dfs(nodeA.right, nodeB.right)
        #如果不同，我们就递归调用主函数来寻找 A 的哪个节点与 B 的根节点匹配。
        return dfs(A, B) or self.isSubStructure(A.left, B) or self.isSubStructure(A.right, B)
