# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """

        def helper(preOrder, postOrder):
            if not preOrder: return None
            if len(preOrder) == 1:
                return TreeNode(preOrder[0])

            root = TreeNode(preOrder[0])  # 根
            inx = postOrder.index(preOrder[1]) + 1  # 左子树根的位置

            root.left = helper(preOrder[1:inx + 1], postOrder[:inx])
            root.right = helper(preOrder[inx + 1:], postOrder[inx:-1])

            return root

        return helper(pre, post)


if __name__ == '__main__':
    solution = Solution()
    #solution.constructFromPrePost([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1])
    li = [4, 5, 2, 6, 7, 3, 1]
    #print(li[0:2])


