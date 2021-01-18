# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findMode(self, root):
        """
        https://leetcode-cn.com/problems/find-mode-in-binary-search-tree/
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        pre, count, maxCount, res = None, 0, 0, []

        def inOrder(node):
            nonlocal count, pre, maxCount
            if not node: return
            inOrder(node.left)

            if not pre:
                count = 1
            elif pre.val == node.val:  # 相当于有序数组的两位两位进行比较
                count += 1
            else:  # 与前一个节点数不一样
                count = 1
            pre = node

            if count == maxCount:
                res.append(node.val)
            if count > maxCount:
                maxCount = count
                res.clear()
                res.append(node.val)

            inOrder(node.right)

        inOrder(root)
        return res
