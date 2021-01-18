# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def longestZigZag(self, root):
        """
        https://leetcode-cn.com/problems/longest-zigzag-path-in-a-binary-tree/
        :type root: TreeNode
        :rtype: int
        """
        ans = 0

        def dfs(node, isLeft, length):
            nonlocal ans
            if not node: return
            ans = max(ans, length)
            if isLeft:
                dfs(node.left, False, length + 1)
                # 如果当前节点应该向左走但是却没有左子树呢？
                # 很无奈那就只能向右了，这个时候 length 的值应该「重置」。
                dfs(node.right, True, 1)
            else:
                dfs(node.right,True,length+1)
                dfs(node.left,False,1)

        dfs(root,True,0)
        dfs(root,False,0)
        return ans


if __name__ == '__main__':
    dicts = {1: 2}
    print(1 in dicts)
